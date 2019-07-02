from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'signup/', views.signup, name='signup'),
    path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.activate, name='activate'),
]