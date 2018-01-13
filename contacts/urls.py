from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from contacts.decorators import user_has_permission
from . import views


app_name = 'contacts'
urlpatterns = [
    url(r'^contact/?$', login_required(views.ContactsListView.as_view()), name='contact_list'),
    url(r'^(?P<contact_id>[0-9]+)/?$', login_required(user_has_permission(views.ContactDetailView.as_view())), name='contact_detail'),
    url(r'^add_contact/?$', login_required(views.AddContactView.as_view()), name='add_contact'),
    url(r'^add_address/?$', login_required(views.AddContactAddressView.as_view()), name='add_address'),
    url(r'^update_contact/(?P<contact_id>[0-9]+)/?$', login_required(user_has_permission(views.UpdateContactView.as_view())), name='update_contact'),
    url(r'^update_contact_address/(?P<address_id>[0-9]+)/?$',
        login_required(user_has_permission(views.UpdateContactAddressView.as_view())), name='update_contact_address'
        ),
    url(r'^delete/(?P<contact_id>\d+)/?$', login_required(user_has_permission(views.DeleteContactView.as_view())), name='delete_contact')
]
