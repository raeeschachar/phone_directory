from functools import wraps
from django.core.exceptions import PermissionDenied

from .models import Contact, Address


def user_added_contact(view_func):
    def _decorator(request, *args, **kwargs):
        if kwargs.get('contact_id') and \
                Contact.objects.filter(pk=kwargs.get('contact_id'), user=request.user).exists():
            return view_func(request, *args, **kwargs)

        elif kwargs.get('address_id') and \
                Address.objects.filter(pk=kwargs.get('address_id'), contact__user=request.user).exists():
            return view_func(request, *args, **kwargs)

        raise PermissionDenied

    return wraps(view_func)(_decorator)
