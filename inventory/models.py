from django.db import models
from management.models import PatientDetails,GeneralVitals_new
from django.db.models import Sum
from dateutil import relativedelta
import datetime
# Create your models here.

class Code_medicine(models.Model):
    medicine_name= models.CharField(max_length=200)
    medicine_brand= models.CharField(max_length=200)
    medicine_id= models.CharField(max_length=30,unique=True)
    min_quantity= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_quantity(self):
        try: 
            x= self.medicine_set.filter(is_active=False).aggregate(Sum('quantity')).get('quantity__sum')
            if x:
                return x
            else:
                return 0
        except:
            return 0



class Medicine(models.Model):
    code=models.ForeignKey(Code_medicine,on_delete=models.CASCADE,null=True,blank=True)
    medicine_name= models.CharField(max_length=200)
    medicine_brand= models.CharField(max_length=200)
    medicine_id= models.CharField(max_length=30,null=True,blank=True)
    quantity= models.IntegerField()
    medicine_mg= models.DecimalField(max_digits = 16, decimal_places = 2)
    medicine_price= models.DecimalField(max_digits = 16, decimal_places = 2)
    stocked_date=models.DateField()
    purchase_date=models.DateField()
    expiry_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField('Is active', default=False)  

    def remaining(self):
        x=relativedelta.relativedelta(self.expiry_date, datetime.datetime.today())
        return x.days

    def __str__(self):
        return f" {self.medicine_brand} brand {self.medicine_name}  details"

    
class Fees(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE,null=True,blank=True)
    vitals=models.ForeignKey(GeneralVitals_new,on_delete=models.CASCADE,null=True,blank=True)
    fees_type= models.CharField(max_length=200,null=True, blank=True)
    fees_amount= models.DecimalField(max_digits = 16, decimal_places = 2,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.patient}  {self.fees_type} fees details"


class Allergy_Medicine(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE,null=True,blank=True)
    vitals=models.ForeignKey(GeneralVitals_new,on_delete=models.CASCADE,null=True,blank=True)
    medicine_name= models.CharField(max_length=200,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.patient} Allergy {self.medicine_name} details"


class Patient_medicine(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE,null=True,blank=True)
    vitals=models.ForeignKey(GeneralVitals_new,on_delete=models.CASCADE,null=True,blank=True)
    medicine_name= models.CharField(max_length=200,null=True, blank=True)
    morning= models.CharField(max_length=200,null=True, blank=True)
    noon= models.CharField(max_length=200,null=True, blank=True)
    evening= models.CharField(max_length=200,null=True, blank=True)
    night= models.CharField(max_length=200,null=True, blank=True)
    days= models.CharField(max_length=200,null=True, blank=True)
    total= models.CharField(max_length=200,null=True, blank=True)
    is_delivered=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.patient} {self.medicine_name} details"
    
class Lab_test(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE,null=True,blank=True)
    vitals=models.ForeignKey(GeneralVitals_new,on_delete=models.CASCADE,null=True,blank=True)
    lab_test=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Symptom(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE,null=True,blank=True)
    vitals=models.ForeignKey(GeneralVitals_new,on_delete=models.CASCADE,null=True,blank=True)
    symptom=models.TextField(null=True, blank=True)
    diagnose=models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class medicine_total_amount(models.Model):
    patient=models.ForeignKey(PatientDetails,on_delete=models.CASCADE,null=True,blank=True)
    vitals=models.ForeignKey(GeneralVitals_new,on_delete=models.CASCADE,null=True,blank=True)
    medicine_total_amount=models.DecimalField(max_digits = 16, decimal_places = 2,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)