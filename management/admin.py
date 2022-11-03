from django.contrib import admin
from .models import ProductDetails,PatientDetails, TodayPatients,GeneralVitals_new 

# admin.site.register(Items_saled)
admin.site.register(ProductDetails)
admin.site.register(PatientDetails)
admin.site.register(GeneralVitals_new) 
admin.site.register(TodayPatients) 

