from django.urls import path

from . import views

urlpatterns = [
 
    path('', views.add_medicine, name='inventory_add_medicine'),
    path('search_medicine/', views.search_medicine, name='inventory_search_medicine'),
    path('update_medicine/', views.update_medicine, name='inventory_update_medicine'),
  
    # path('register/', views.register, name='register'),  

]