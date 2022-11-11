from django.urls import path

from . import views

urlpatterns = [
 
    path('', views.add_medicine, name='inventory_add_medicine'),
    path('search_medicine/', views.search_medicine, name='inventory_search_medicine'),
    path('update_medicine/', views.update_medicine, name='inventory_update_medicine'),
    path('doctor/', views.doctor, name='inventory_doctor'),
    path('add_code/', views.add_code, name='inventory_add_code'),
    path('medicine_amount/', views.medicine_amount, name='inventory_medicine_amount'),
    path('medicine_quantity/', views.medicine_quantity, name='inventory_medicine_quantity'),
    path('patients/', views.patients, name='inventory_patients'),
    path('lab_test/<int:id>/', views.lab_test, name='inventory_lab_test'),
    path('prescription/<int:id>/', views.prescription, name='inventory_prescription'),
    path('update_code/',views.update_code, name='inventory_update_code'),
    path('delete_code/',views.delete_code, name='inventory_delete_code'),
    path('medicine_bill/',views.medicine_bill, name='inventory_medicine_bill'),
    
]