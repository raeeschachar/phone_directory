from django.conf.urls import url

from phone_directory import settings
from django.views.static import serve
from . import views


app_name = 'contacts'
urlpatterns = [
    url(r'^$', views.ContactsListView.as_view(), name='contact'),
    url(r'^(?P<pk>[0-9]+)/?$', views.ContactDetailView.as_view(), name='detail'),
    url(r'^add_contact/?$', views.AddContactView.as_view(), name='add_contact'),
    url(r'^add_address/?$', views.AddContactAddressView.as_view(), name='add_address'),
    url(r'^update_contact/(?P<pk>[0-9]+)/?$', views.UpdateContactView.as_view(), name='update_contact'),
    url(r'^update_contact_address/(?P<pk>[0-9]+)/?$',
        views.UpdateContactAddressView.as_view(), name='update_contact_address'
        )
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
    ]
