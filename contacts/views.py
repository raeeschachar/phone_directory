from django.views import generic
from .models import Contact
from django.views.generic.edit import CreateView


class ContactsListView(generic.ListView):
    context_object_name = 'my_contacts'
    queryset = Contact.objects.order_by('name')


class ContactDetailView(generic.DetailView):
    model = Contact


class AddContactView(CreateView):
    model = Contact
    fields = ['name', 'email', 'phone_number']

    success_url = "/contacts"
