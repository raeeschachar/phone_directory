from django.conf.urls import url

from . import views


app_name = 'contacts'
urlpatterns = [
    url(r'^$', views.ContactView.as_view(), name='contact')
]
