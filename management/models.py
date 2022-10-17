from sqlite3 import Date
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    address=models.TextField()
    aadhar_number=models.IntegerField()
    phone_number=models.IntegerField()
    is_admin = models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is_customer', default=False)



class ProductDetails(models.Model):
    product_name= models.CharField(max_length=30)
    product_id= models.CharField(max_length=30)
    product_quantity= models.CharField(max_length=30)
    product_price= models.CharField(max_length=30)
    expiry_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=   models.BooleanField('Is active', default=False)  
 

class Items_saled(models.Model):
    item = models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    items_saled=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PatientDetails(models.Model):
    patient_id= models.CharField(max_length=30)
    patient_name= models.CharField(max_length=30)
    fathers_name= models.CharField(max_length=30)
    age= models.IntegerField()
    date_of_birth= models.DateField()
    gender= models.CharField(max_length=30)
    address= models.TextField(max_length=30)
    phone_number = models.IntegerField(null=True,blank=True)
   
     


class TodayPatients(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=   models.BooleanField('Is active', default=False) 

    def __str__(self):
        return f'{self.patient.patient_name}'

class HealthHistory(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    treatment_details = models.TextField()

    def __str__(self):
        return f'{self.patient.patient_name}'



class PrescribedMedicine(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE)
    reason=models.TextField(max_length=30)
    medicine_name=models.CharField(max_length=30)
    treatment_details=models.TextField()
    quantity=models.IntegerField()

class BillsModel(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE)
    price=models.IntegerField()
    amount=models.IntegerField()
    bill_no = models.CharField(max_length=500, null=True, blank=True)
    

    def __str__(self):
        return f'{self.patient.patient_name}'

class GeneralVitals(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE,null=True,blank=True)
    temperature=models.IntegerField()
    pulse_rate=models.IntegerField()
    blood_pressure=models.IntegerField()
    height=models.FloatField()
    weight=models.FloatField()
    others=models.TextField()








   







