from django.conf import settings
from django.contrib import auth
from datetime import datetime, timedelta


class AutoLogout(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated():
            try:
                if datetime.now() - request.session['last_touch'] > timedelta(0, settings.AUTO_LOGOUT_DELAY * 60, 0):
                    auth.logout(request)
                    del request.session['last_touch']
                    response = self.get_response(request)
                    return response

            except KeyError:
                pass
            request.session['last_touch'] = datetime.now()
        response = self.get_response(request)
        return response
