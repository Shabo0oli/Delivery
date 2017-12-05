from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/register/?$', views.register, name='register'),
    url(r'^accounts/registerSeller/?$', views.registerSeller, name='registerSeller'),
    url(r'^accounts/addproduct/?$', views.addproduct, name='addproduct'),
    url(r'^search/$', views.search, name='search'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^showdetail/([0-9]*)/$', views.show_detail, name='showdetail'),
    url(r'^addcomment/$', views.add_comment, name='add_comment'),
    url(r'^preorder/([0-9]*)/$', views.preorder, name='preorder'),
    url(r'^myorder/$', views.myorder, name='myorder'),
    url(r'^submitedpreorder/$', views.submitedpreorder, name='submitedpreorder'),
    url(r'^mypreorder/$', views.mypreorder, name='mypreorder'),
    url(r'^submitpreorder/$', views.submitpreorder, name='submitpreorder'),
    url(r'^submitedorder/$', views.submitedorder, name='submitedorder'),
    url(r'^showbasket/$', views.showbasket, name='showbasket'),
    url(r'^addtobasket/([0-9]*)/$', views.addtobasket, name='addtobasket'),
    url(r'^accounts/login/?$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^$', views.index, name='index'),
]