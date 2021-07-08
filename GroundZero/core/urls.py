from django.urls import path
from . import views
from .views import home, crearproveedor, Ver, form_mod_proveedor, Ingresar, form_del_proveedor
from django.conf.urls import url

urlpatterns=[                                               
    path('',home, name='home'),
    path('form_crearproveedor', Ingresar, name="form_crearproveedor"),
    path('ver', Ver, name='ver'),
    path('form_mod_proveedor/<idproveedor>', form_mod_proveedor, name="form_mod_proveedor"), 
    path('form_del_proveedor/<idproveedor>', form_del_proveedor, name="form_del_proveedor"),
    url('ver.html', Ver ,name='ver.html'),
    url('home.html', home ,name='home.html')
]

