from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic, View

from contacts.forms import NewContactForm, LoginForm
from .models import Contact, Address


class ContactsListView(generic.ListView):
    context_object_name = 'my_contacts'
    queryset = Contact.objects.order_by('name')


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
            return HttpResponseRedirect(reverse('contacts:contact'))
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


class AddContactAddressView(generic.CreateView):
    model = Address
    fields = ['contact', 'address_selection', 'address_line', 'city', 'state', 'zip_code', 'country']
    success_url = reverse_lazy('contacts:contact')


class UpdateContactView(generic.UpdateView):
    model = Contact
    fields = ['name', 'email', 'phone_number', 'contact_image']

    def get_success_url(self):
        return reverse('contacts:detail', kwargs={'pk': self.get_object().id})


class UpdateContactAddressView(generic.UpdateView):
    model = Address
    fields = ['contact', 'address_selection', 'address_line', 'city', 'state', 'zip_code', 'country']

    def get_success_url(self):
        return reverse('contacts:detail', kwargs={'pk': self.get_object().contact.id})


class DeleteContactView(View):
    template_name = "contacts/delete_contact.html"

    def get(self, request, pk):
        return render(request, self.template_name, {'object': Contact.objects.get(id=pk)})

    def post(self, request, pk):
        contact = Contact.objects.get(id=pk)
        contact.delete()
        return HttpResponseRedirect(reverse('contacts:contact'))


class LoginView(View):
    form_class = LoginForm
    template_name = 'contacts/login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=un, password=pw)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('contacts:contact'))
                else:
                    print("Invalid account")
                    return HttpResponseRedirect(reverse('contacts:user_login'))
            else:
                print("The username and password were incorrect")
                return HttpResponseRedirect(reverse('contacts:user_login'))
        else:
            return render(request, self.template_name, {'form': form})


class HomePageView(View):
    template_name = 'contacts/home.html'

    def get(self, request):
        return render(request, self.template_name)


class LogoutView(View):
    template_name = 'contacts/home.html'

    def get(self, request):
        return render(request, self.template_name)
