from django.views import generic
from .models import Contact, Address


class ContactsListView(generic.ListView):
    context_object_name = 'my_contacts'
    queryset = Contact.objects.order_by('name')


class ContactDetailView(generic.DetailView):
    model = Contact


class AddContactView(generic.CreateView):
    model = Contact
    fields = ['name', 'email', 'phone_number']


class AddContactAddressView(generic.CreateView):
    model = Address
    fields = ['contact', 'address_selection', 'address_line', 'city', 'state', 'zip_code', 'country']
