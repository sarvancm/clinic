from django.urls import path

from . import views

urlpatterns = [
 
    path('', views.add_medicine, name='inventory_add_medicine'),
    path('search_medicine/', views.search_medicine, name='inventory_search_medicine'),
  
    # path('register/', views.register, name='register'),  

]