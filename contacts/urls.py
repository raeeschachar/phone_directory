from django.conf.urls import url

from . import views


app_name = 'contacts'
urlpatterns = [
    url(r'^contact/?$', views.ContactsListView.as_view(), name='contact_list'),
    url(r'^(?P<pk>[0-9]+)/?$', views.ContactDetailView.as_view(), name='contact_detail'),
    url(r'^add_contact/?$', views.AddContactView.as_view(), name='add_contact'),
    url(r'^add_address/?$', views.AddContactAddressView.as_view(), name='add_address'),
    url(r'^update_contact/(?P<pk>[0-9]+)/?$', views.UpdateContactView.as_view(), name='update_contact'),
    url(r'^update_contact_address/(?P<pk>[0-9]+)/?$',
        views.UpdateContactAddressView.as_view(), name='update_contact_address'
        ),
    url(r'^delete/(?P<pk>\d+)/?$', views.DeleteContactView.as_view(), name='delete_contact')
]
