from django.shortcuts import render
from django.views import generic
from .models import Contact, Address


class ContactView(generic.ListView):
    template_name = 'contacts/contact.html'
    context_object_name = 'my_contacts'

    def get_queryset(self):
        """
        Return contacts by name
        """
        return Contact.objects.order_by('name')


# class DetailView(generic.DetailView):
#     model = Contact
#     template_name = 'contacts/detail.html'
#
#     def get_queryset(self):
#         """
#         Return details of contact
#         """
#         return Contact.objects.get(id=Contact.id)


def detail(request, contact_id):
    contact_details = Contact.objects.get(id=contact_id)
    address_details = Address.objects.get(id=contact_id)
    return render(request, 'contacts/detail.html', {
        'contact_details': contact_details, 'address_details': address_details
    })
