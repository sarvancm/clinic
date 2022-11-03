from django.contrib import admin
from .models import Medicine,Fees,Symptom,Lab_test,Patient_medicine,Allergy_Medicine,Code_medicine

# Register your models here.


admin.site.register(Medicine)
admin.site.register(Fees)
admin.site.register(Symptom)
admin.site.register(Lab_test)
admin.site.register(Patient_medicine)
admin.site.register(Allergy_Medicine)
admin.site.register(Code_medicine)