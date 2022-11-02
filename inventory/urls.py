from django.urls import path

from . import views

urlpatterns = [
 
    path('', views.add_medicine, name='inventory_add_medicine'),
    path('search_medicine/', views.search_medicine, name='inventory_search_medicine'),
    path('update_medicine/', views.update_medicine, name='inventory_update_medicine'),
    path('doctor/', views.doctor, name='inventory_doctor'),
    path('medicine_amount/', views.medicine_amount, name='inventory_medicine_amount'),
    path('previous_medicine/', views.previous_medicine, name='inventory_previous_medicine'),
    path('next_medicine/', views.next_medicine, name='inventory_next_medicine'),
    path('patients/', views.patients, name='inventory_patients'),
  
    # path('register/', views.register, name='register'),  

]