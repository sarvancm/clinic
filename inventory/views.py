from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import Medicine,Fees,Allergy_Medicine,Patient_medicine,Lab_test
import datetime
from django.db.models import Q
from django.http import JsonResponse
import json
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt
from management.models import AddFees 


# Create your views here.

# add_medicine
def add_medicine(request):

    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'medicine added successfully')
            form = MedicineForm()
            return render(request,'inventory/add_medicine.html', {'add':True,'form': form,'medicine':incrementid()})
        else:
            return render(request,'inventory/add_medicine.html', {'add':True,'form': form,'medicine':incrementid()})
    else:
        form = MedicineForm()
        return render(request,'inventory/add_medicine.html', {'add':True,'form': form,'medicine':incrementid()})


# search_medicine
def search_medicine(request):
    if request.method == 'POST':
        name_id=request.POST.get('search')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        medi=Medicine.objects.filter(Q(medicine_name=name_id)|Q(medicine_id=name_id))
        medi_id=[i.id for i in medi] 
        try:
            a = datetime.datetime.strptime( start_date, '%Y-%m-%d').date()
            b = datetime.datetime.strptime( end_date, '%Y-%m-%d').date()
            medicines=Medicine.objects.filter(created_at__date__gte=a,created_at__date__lte=b)
        except:
            a=start_date
            b=end_date
            medicines=[]
        if medi_id and medicines:
            medicines=[i for i in medicines if i.id in medi_id]
        elif medi:
            medicines=medi
        else:
            medicines = medicines

        return render(request,'inventory/search_medicine.html', {'search':True,'medicines': medicines,'name_id':name_id,'start_date':start_date,'end_date':end_date})
    else:

        return render(request,'inventory/search_medicine.html', {'search':True})


# update_medicine
def update_medicine(request):

    if request.method == 'POST':
        id = request.POST.get('object_id')
        name_id=request.POST.get('search')
        start_date=request.POST.get('start_date')
        end_date=request.POST.get('end_date')
        
        object=Medicine.objects.get(id=id)
        form = MedicineForm(request.POST,instance=object)
        if form.is_valid():
            form.save()
            messages.success(request, 'medicine updated successfully')
            medi=Medicine.objects.filter(Q(medicine_name=name_id)|Q(medicine_id=name_id))
            medi_id=[i.id for i in medi] 
            try:
                a = datetime.datetime.strptime( start_date, '%Y-%m-%d').date()
                b = datetime.datetime.strptime( end_date, '%Y-%m-%d').date()
                medicines=Medicine.objects.filter(created_at__date__gte=a,created_at__date__lte=b)
            except:
                a=start_date
                b=end_date
                medicines=[]
            if medi_id and medicines:
                medicines=[i for i in medicines if i.id in medi_id]
            elif medi:
                medicines=medi
            else:
                medicines = medicines
            return render(request,'inventory/search_medicine.html', {'search':True,'medicines': medicines,'name_id':name_id,'start_date':start_date,'end_date':end_date})

        else:
            medi=Medicine.objects.filter(Q(medicine_name=name_id)|Q(medicine_id=name_id))
            medi_id=[i.id for i in medi] 
            try:
                a = datetime.datetime.strptime( start_date, '%Y-%m-%d').date()
                b = datetime.datetime.strptime( end_date, '%Y-%m-%d').date()
                medicines=Medicine.objects.filter(created_at__date__gte=a,created_at__date__lte=b)
            except:
                a=start_date
                b=end_date
                medicines=[]
            if medi_id and medicines:
                medicines=[i for i in medicines if i.id in medi_id]
            elif medi:
                medicines=medi
            else:
                medicines = medicines
            return render(request,'inventory/search_medicine.html', {'search':True,'object':id,'err':True,'form':form,'medicines': medicines,'name_id':name_id,'start_date':start_date,'end_date':end_date})

    else:
        
        return redirect('inventory_search_medicine')


def doctor(request):
    if request.method == "POST": 
        data = json.loads(request.body)
        patient_object=data['patient_object']
        vital_object=data['vital_object']
        fees=data['consulting']['consulting']
        allergy=data['allergy']['Allergy']
        prescription=data['prescription']['Prescription']
        labtesting=data['lab_testing']['LabTesting']
   
        
        for i in fees:
            Fees.objects.create(patient_id=patient_object,vitals_id=vital_object,fees_type=i['Consulting'],fees_amount=i['Amount'])

        for i in allergy:
            Allergy_Medicine.objects.create(patient_id=patient_object,vitals_id=vital_object,medicine_name=i['Allergy\xa0Medicine'])
            
        for i in prescription:
            Patient_medicine.objects.create(patient_id=patient_object,vitals_id=vital_object,medicine_name=i['Medicine\xa0Name'],morning=i['Morning'],noon=i['After\xa0Noon'],
            evening=i['Evening'],night=i['Night'],days=i['Days'],total=i['Total'],symptom=data['patient_symptom'],diagnose=data['patient_diagnose'])

        for i in labtesting:
            Lab_test.objects.create(patient_id=patient_object,vitals_id=vital_object,lab_test=i['Tests'])
            
        data={}
        return JsonResponse(data)
   

def medicine_amount(request):
    if request.method == "POST": 
        id = request.POST.get('consultingName')
        amount=AddFees.objects.get(id=id)
        amount=amount.amount
        data ={'data':amount}
        return JsonResponse(data)


def patients(request):
    if request.method == "POST": 
        id = request.POST.get('name')
        data ={}
        return JsonResponse(data)
    else:
        x= [Patient_medicine.objects.get(vitals_id=j) for j in {i.vitals_id for i in Patient_medicine.objects.filter(created_at__contains=datetime.datetime.today().date())}]
        return render(request,'inventory/patients.html',{'x':x})

def previous_medicine(request):
    if request.method == "POST": 
        id = request.POST.get('name')
        data ={}
        return JsonResponse(data)

def next_medicine(request):
    if request.method == "POST": 
        id = request.POST.get('name')
        data ={}
        return JsonResponse(data)


def incrementid():
    last = Medicine.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "MD022" "%04d" % last)

