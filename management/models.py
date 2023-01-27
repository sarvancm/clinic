from enum import unique
from sqlite3 import Date
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from dateutil import relativedelta
from datetime import date



class User(AbstractUser):
    address=models.TextField(null=True,blank=True)
    aadhar_number=models.BigIntegerField(null=True,blank=True)
    pan_number=models.CharField(max_length=30,null=True,blank=True)
    phone_number=models.IntegerField(null=True,blank=True)
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
    age= models.CharField(max_length=30)
    date_of_birth= models.DateField()
    gender= models.CharField(max_length=30)
    blood_group=models.CharField(max_length=30,null=True,blank=True)
    address= models.TextField(max_length=30)
    phone_number = models.IntegerField(null=True,blank=True,error_messages={'phone_number':'Enter a valid phone number'})
   
   
    @property
    def age_patient(self):
        
            
            date_of_birth = self.date_of_birth
            birth=datetime.strptime(str(date_of_birth), '%Y-%m-%d')
            
            current = date.today()
            diff=relativedelta.relativedelta(current, birth)
            if diff.years > 0:
                age=f'{diff.years} years'
            elif diff.months >0:
                age=f'{diff.months} months'
            elif diff.days >0:
                age=f'{diff.days} days'
            elif diff.hours >0:
                age=f'{diff.hours} hours'
            else:
                age= 'less than a hour'

            return age
            
           



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


    


class AddFees(models.Model):
    fee_name=models.CharField(max_length=30,unique=True)
    amount=models.DecimalField(max_digits=15, decimal_places=2)


class GeneralVitals_new(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE,null=True,blank=True)
    temperature=models.FloatField()
    pulse_rate=models.IntegerField()
    blood_pressure_start=models.IntegerField()
    blood_pressure_end=models.IntegerField()
    height=models.FloatField()
    weight=models.FloatField()
    others=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_consulted=   models.BooleanField(default=False)



class TodayPatients(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=   models.BooleanField('Is active', default=False) 
    is_vital=   models.BooleanField(default=False)
    is_consulted=   models.BooleanField(default=False)
    is_seperated=models.BooleanField(default=False)
    vitals=models.ForeignKey(GeneralVitals_new,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.patient.patient_name}'


   







