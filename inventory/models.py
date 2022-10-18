from django.db import models

# Create your models here.

class Medicine(models.Model):
    medicine_name= models.CharField(max_length=200)
    medicine_brand= models.CharField(max_length=200)
    medicine_id= models.CharField(max_length=30)
    quantity= models.IntegerField()
    medicine_mg= models.DecimalField(max_digits = 16, decimal_places = 2)
    medicine_price= models.DecimalField(max_digits = 16, decimal_places = 2)
    stocked_date=models.DateField()
    purchase_date=models.DateField()
    expiry_date=models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active=models.BooleanField('Is active', default=False)  

    def __str__(self):
        return f" {self.medicine_brand} brand {self.medicine_name}  details"