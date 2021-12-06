from django.urls import path
from . import views

app_name='home'

urlpatterns= [
    path('',views.home,name='home'),
    path('accion/',views.boton,name='boton'),
    path('accion2/',views.siguiente,name='siguiente'),
]