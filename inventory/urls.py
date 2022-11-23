from django.urls import path

from . import views

urlpatterns = [
 
    path('', views.add_medicine, name='inventory_add_medicine'),
    path('search_medicine/', views.search_medicine, name='inventory_search_medicine'),
    path('update_medicine/', views.update_medicine, name='inventory_update_medicine'),
    path('doctor/', views.doctor, name='inventory_doctor'),
    path('add_code/', views.add_code, name='inventory_add_code'),
    path('add_medicine_code/', views.add_medicine_code, name='inventory_add_medicine_code'),
    path('medicine_amount/', views.medicine_amount, name='inventory_medicine_amount'),
    path('medicine_quantity/', views.medicine_quantity, name='inventory_medicine_quantity'),
    path('patients/', views.patients, name='inventory_patients'),
    path('lab_test/<int:id>/', views.lab_test, name='inventory_lab_test'),
    path('lab_test/<int:id>/<str:printer>/', views.lab_test, name='inventory_lab_test'),
    path('out_medicine/<int:id>/', views.out_medicine, name='inventory_out_medicine'),
    path('out_medicine/<int:id>/<str:printer>/', views.out_medicine, name='inventory_out_medicine'),
    path('consult_fees/<int:id>/', views.consult_fees, name='inventory_consult_fees'),
    path('consult_fees/<int:id>/<str:printer>/', views.consult_fees, name='inventory_consult_fees'),
    path('prescription/<int:id>/', views.prescription, name='inventory_prescription'),
    path('update_code/',views.update_code, name='inventory_update_code'),
    path('delete_code/',views.delete_code, name='inventory_delete_code'),
    path('medicine_bill/<int:id>/',views.medicine_bill, name='inventory_medicine_bill'),
    path('medicine_bill/<int:id>/<str:printer>/',views.medicine_bill, name='inventory_medicine_bill'),
    
]