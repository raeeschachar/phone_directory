from django.core.exceptions import PermissionDenied
from .models import Contact
from functools import wraps


def user_added_contact(view_func):
    def _decorator(request, *args, **kwargs):

        if Contact.objects.get(pk=kwargs['contact_id'], user = request.user).exist():
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wraps(view_func)(_decorator)
