from django.conf.urls import url

from . import views


app_name = 'contacts'
urlpatterns = [
    url(r'^$', views.ContactsListView.as_view(), name='contact'),
    url(r'^(?P<pk>[0-9]+)/?$', views.ContactDetailView.as_view(), name='detail'),
    url(r'^add_contact/?$', views.AddContactView.as_view(), name='add_contact'),
]
