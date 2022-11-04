from django.urls import path

from . import views

urlpatterns = [
 
    path('', views.add_medicine, name='inventory_add_medicine'),
    path('search_medicine/', views.search_medicine, name='inventory_search_medicine'),
    path('update_medicine/', views.update_medicine, name='inventory_update_medicine'),
    path('doctor/', views.doctor, name='inventory_doctor'),
    path('medicine_amount/', views.medicine_amount, name='inventory_medicine_amount'),
    path('add_medicine_code/', views.add_medicine_code, name='inventory_add_medicine_code'),
    path('patients/', views.patients, name='inventory_patients'),
    path('lab_test/', views.lab_test, name='inventory_lab_test'),
    path('prescription/', views.prescription, name='inventory_prescription'),
    

]