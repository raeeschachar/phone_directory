from django.conf.urls import url

from . import views


app_name = 'user_sessions'
urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^user_sessions/?$', views.LoginView.as_view(), name='login'),
    url(r'^logout/?$', views.LogoutView.as_view(), name='logout')
]
