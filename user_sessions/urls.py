from django.conf.urls import url

from . import views


app_name = 'user_sessions'
urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^login/?$', views.LoginView.as_view(), name='login'),
    url(r'^logout/?$', views.LogoutView.as_view(), name='logout'),
    url(r'^register_user/?$', views.AddUserView.as_view(), name='register_user')
]
