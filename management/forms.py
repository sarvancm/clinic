from dataclasses import fields
from django import forms
from msilib.schema import Class
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import User,Items_saled,ProductDetails,PatientDetails,HealthHistory,PrescribedMedicine,BillsModel,GeneralVitals_new,AddFees 
from django.core.exceptions import ValidationError




class RegisterForm(UserCreationForm):
   
   class Meta:
        model=User
        fields=['first_name','last_name','username','phone_number','aadhar_number','pan_number','email','address','password1','password2']
        labels={'email':'Email'}



class InputForm(forms.ModelForm):   
   class Meta:
        model=Items_saled
        fields='__all__'

class ProductDetailsForm(forms.ModelForm):  
   # my_field = DateField(widget = AdminDateWidget) 
   # expiry_date = forms.DateField(attrs={'type':'date'})
   class Meta:
      model=ProductDetails
      fields=['product_name','product_id','product_quantity','product_price','expiry_date']
      
 

      widgets = { 'expiry_date' : forms.DateInput(attrs={'type':'date',}),}

class PatientDetailsForm(forms.ModelForm):   
   class Meta:
      model=PatientDetails
      fields = '__all__'
      widgets = {
         'date_of_birth': forms.DateInput(attrs={'type': 'date'})
      }

      # def clean_phone_number(self):
      #    phone_number = self.cleaned_data['phone_number']
      #    print(phone_number)
      #    #   try:
      #    #       x=int(phone_number)
      #    #       count=len(str(x))
      #    #       if count!=10:
      #    #          raise ValidationError("Enter a valid 10 digit phone number")
               
      #    #   except:
      #    #       raise ValidationError("Enter a valid phone number")

      #    return phone_number
        
   def __init__(self,*args,**kwargs):
      super().__init__(*args,**kwargs)
      for field in self.fields.values():
         field.widget.attrs['class']='form-control'


class HistoryForm(forms.ModelForm):
    class Meta:
        model = HealthHistory
        fields = '__all__'

class MedicineDetailForm(forms.ModelForm):
   class Meta:
      model =PrescribedMedicine
      fields = '__all__'

class BillsModelForm(forms.ModelForm):
   class Meta:
      model=BillsModel
      fields = ['price','amount']

# class BirthFieldForm(forms.ModelForm):
#    class Meta:
#       model=BirthField
#       fields=['date_of_birth']

class GeneralVitals_newForm(forms.ModelForm):
   class Meta:
      model= GeneralVitals_new
      fields = '__all__'

class AddFeesForm(forms.ModelForm):
   class Meta:
      model=AddFees
      fields = '__all__'





