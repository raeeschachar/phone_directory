from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic, View

from contacts.forms import NewContactForm, NewAddressForm
from .models import Contact, Address


class ContactsListView(View):
    template_name = "contacts/contact_list.html"

    def get(self, request):
        specific = Contact.objects.filter(user=request.user)
        return render(request, self.template_name, {'user_specific_contacts': specific})


class ContactDetailView(generic.DetailView):
    model = Contact


class AddContactView(View):
    form_class = NewContactForm
    template_name = 'contacts/contact_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()
            return HttpResponseRedirect(reverse('contacts:contact_list'))
        return render(request, self.template_name, {'form': form})


"""This one works too"""
# def add_contact_view(request):
#     if request.method == 'POST':
#         form = NewContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return HttpResponseRedirect(reverse('contacts:contact'))
#     else:
#         form = NewContactForm()
#         return render(request, 'contacts/contact_form.html', {'form': form})

"""This one works too"""
# class AddContactView(generic.CreateView):
#     model = Contact
#     fields = ['name', 'email', 'phone_number']
#     success_url = reverse_lazy('contacts:contact')


class AddContactAddressView(View):
    form_class = NewAddressForm
    template_name = 'contacts/address_form.html'

    def get(self, request):
        form = self.form_class()
        form.fields.get('contact').queryset=Contact.objects.filter(user=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return HttpResponseRedirect(reverse('contacts:contact_list'))
        return render(request, self.template_name, {'form': form})


class UpdateContactView(generic.UpdateView):
    model = Contact
    fields = ['name', 'email', 'phone_number', 'contact_image']

    def get_success_url(self):
        return reverse('contacts:contact_detail', kwargs={'pk': self.get_object().id})


class UpdateContactAddressView(generic.UpdateView):
    model = Address
    fields = ['address_selection', 'address_line', 'city', 'state', 'zip_code', 'country']

    def get_success_url(self):
        return reverse('contacts:contact_detail', kwargs={'pk': self.get_object().contact.id})


class DeleteContactView(View):
    template_name = "contacts/delete_contact.html"

    def get(self, request, pk):
        return render(request, self.template_name, {'object': Contact.objects.get(id=pk)})

    def post(self, request, pk):
        contact = Contact.objects.get(id=pk)
        contact.delete()
        return HttpResponseRedirect(reverse('contacts:contact_list'))
