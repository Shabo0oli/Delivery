from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/register/?$', views.register, name='register'),
    url(r'^accounts/registerSeller/?$', views.registerSeller, name='registerSeller'),
    url(r'^accounts/login/?$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', views.index, name='index'),
]