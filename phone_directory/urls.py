from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from phone_directory import settings

urlpatterns = [
    url(r'^contacts/', include('contacts.urls')),
    url(r'^', include('user_sessions.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
