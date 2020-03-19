
from django.urls import path
from . import views

urlpatterns = [
    path('',views.showall,name='show'),
    path('create/',views.create,name='create'),
    path('product/<str:pk>/',views.calproduct,name='product'),
    path('calamount/<str:pk>/',views.calamount,name='amount'),
]