from django.contrib import admin
from .models import ProductDetails,PatientDetails,GeneralVitals, TodayPatients 

# admin.site.register(Items_saled)
admin.site.register(ProductDetails)
admin.site.register(PatientDetails)
admin.site.register(GeneralVitals) 
admin.site.register(TodayPatients) 

