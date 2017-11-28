from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/register/?$', views.register, name='register'),
    url(r'^accounts/registerSeller/?$', views.registerSeller, name='registerSeller'),
    url(r'^accounts/addproduct/?$', views.addproduct, name='addproduct'),
    url(r'^search/$', views.search, name='search'),
    url(r'^showbasket/$', views.showbasket, name='showbasket'),
    url(r'^addtobasket/([0-9]*)/$', views.addtobasket, name='addtobasket'),
    url(r'^accounts/login/?$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', views.index, name='index'),
]