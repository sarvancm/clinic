from django.contrib import admin
from django.apps import apps
from .models import *

# admin.site.register(Items_saled)
admin.site.register(ProductDetails)
admin.site.register(PatientDetails)
admin.site.register(GeneralVitals_new) 
admin.site.register(TodayPatients) 


post_models = apps.get_app_config('management').get_models()

for model in post_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
