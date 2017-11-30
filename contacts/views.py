from django.views import generic
from .models import Contact


class ContactView(generic.ListView):
    template_name = 'contacts/contact.html'
    context_object_name = 'my_contacts'

    def get_queryset(self):
        """
        Return contacts by name
        """
        return Contact.objects.order_by('name')
