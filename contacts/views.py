from django.views import generic
from .models import Contact


class ContactsListView(generic.ListView):
    context_object_name = 'my_contacts'
    queryset = Contact.objects.order_by('name')


class ContactDetailView(generic.DetailView):
    model = Contact


class AddContactView(generic.CreateView):
    model = Contact
    fields = ['name', 'email', 'phone_number']
