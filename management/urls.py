from django.urls import path

from . import views

urlpatterns = [
 
    path('dashboard/', views.navbar, name='navbar'),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login_view', views.login_view, name='login_view'),
    path('logout/', views.user_logout, name='user_logout'),
    path('create_product_details/', views.create_product_details, name='create_product_details'),
    path('list_product_details/', views.list_product_details, name='list_product_details'),
   
    path('view_product_details/<int:id>/', views.view_product_details, name='view_product_details'),
    path('enable_product_details/<int:id>/', views.enable_product_details, name='enable_product_details'),
    path('disable_product_details/<int:id>/', views.disable_product_details, name='disable_product_details'),

    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),

    path('edit_product_details/<int:id>/',views.edit_product_details,name='edit_product_details'),

   
    path('sale/', views.sale, name='sale'),
    path('patients_register/', views.patients_register, name='patients_register'),

    path('search_patient/', views.search_patient, name='search_patient'),
    path('update_patient_details/', views.update_patient_details, name='update_patient_details'),
    path('bills/', views.update_patient_details, name='update_patient_details'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('user_view/', views.user_view, name='user_view'),
    path('disable_view/<int:id>/', views.disable_view, name='disable_view'),
    path('enable_view/<int:id>/', views.enable_view, name='enable_view'),
   
   
    path('past_history/<int:id>/', views.past_history, name='past_history'),
    path('medicine_details/<int:id>/',views.medicine_details, name='medicine_details'),
    path('bill_detail/<int:id>/',views.bills, name='bills'),
    path('edit_bills/<int:id>/',views.edit_bills, name='edit_bills'),
    path('click_patient/<int:id>/<str:name>/',views.click_patient, name='click_patient'),
    path('click_patient/<int:id>/',views.click_patient, name='click_patient'),
    path('general_vitals/',views.general_vitals, name='general_vitals'),
    path('doctor_view/<int:id>/',views.doctor_view, name='doctor_view'),
     path('doctor_view/',views.doctor_view, name='doctor_view'),
     path('doctor_vie/<int:id>/',views.doctor_vie, name='doctor_vie'),
     path('fee_mode/',views.fee_mode, name='fee_mode'),

     path('add_fees/',views.add_fees, name='add_fees'),
     path('delete_fees/',views.delete_fees, name='delete_fees'),




   



    







   





    
    



]