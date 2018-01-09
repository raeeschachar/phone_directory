from functools import wraps
from django.core.exceptions import PermissionDenied

from .models import Contact


def user_added_contact(view_func):
    def _decorator(request, *args, **kwargs):
        if Contact.objects.filter(pk=kwargs.get('pk'), user=request.user).exists():
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wraps(view_func)(_decorator)
