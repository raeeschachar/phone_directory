from django.urls import reverse_lazy, reverse
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
    success_url = reverse_lazy('contacts:contact')


class AddContactAddressView(generic.CreateView):
    model = Address
    fields = ['contact', 'address_selection', 'address_line', 'city', 'state', 'zip_code', 'country']
    success_url = reverse_lazy('contacts:contact')


class UpdateContactView(generic.UpdateView):
    model = Contact
    fields = ['name', 'email', 'phone_number']

    def get_success_url(self):
        return reverse('contacts:detail', kwargs={'pk': self.get_object().id})


class UpdateContactAddressView(generic.UpdateView):
    model = Address
    fields = ['contact', 'address_selection', 'address_line', 'city', 'state', 'zip_code', 'country']

    def get_success_url(self):
        return reverse('contacts:detail', kwargs={'pk': self.get_object().contact.id})
