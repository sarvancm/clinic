from django import forms
from .models import Medicine






class MedicineForm(forms.ModelForm):  
   class Meta:
      model=Medicine
      fields='__all__'

      widgets = { 'expiry_date' : forms.DateInput(attrs={'type':'date',}),
                    'stocked_date' : forms.DateInput(attrs={'type':'date',}),
                    'purchase_date' : forms.DateInput(attrs={'type':'date',}),
                    }

   def __init__(self,*args,**kwargs):
         super().__init__(*args,**kwargs)
         for field in self.fields.values():
               field.widget.attrs['class']='form-control'