from django.conf.urls import url

from . import views


app_name = 'contacts'
urlpatterns = [
    url(r'^$', views.ContactView.as_view(), name='contact'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^([0-9]+)/$', views.detail, name='detail')
]
