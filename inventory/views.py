from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import MedicineForm,CodeForm
from .models import Medicine,Fees,Allergy_Medicine,Patient_medicine,Lab_test,Symptom,Code_medicine,medicine_total_amount
import datetime
from django.db.models import Q
from django.http import JsonResponse
import json
from pprint import pprint
from django.views.decorators.csrf import csrf_exempt
from management.models import AddFees,TodayPatients,GeneralVitals_new
from django.contrib.auth.decorators import login_required
from django.db.models import Sum




# Create your views here.

@login_required(login_url='login_view')
def add_code(request):
    addfees= Code_medicine.objects.all()    
    if request.method=="POST":
        amount=request.POST.get('amount')
        form=CodeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'created successfully')
            return redirect('inventory_add_code') 
        else:
            return render(request,"inventory/add_code.html",{'addfees':addfees,'form':form}) 
    else:
        form=CodeForm()
        return render(request,"inventory/add_code.html",{'addfees':addfees,'form':form})


@login_required(login_url='login_view')
def update_code(request):
    if request.method=="POST":
        object=request.POST.get("ob")
        name=request.POST.get("medicine_id")
        amount=request.POST.get("medicine_name")
        brand=request.POST.get("medicine_brand")
        z=Code_medicine.objects.get(id=object)
        form1=CodeForm(request.POST,instance=z)          
        if form1.is_valid():
            z.medicine_id= name
            z.medicine_name=  amount 
            z.medicine_brand=  brand 
            z.save()   
            messages.success(request, f'{z.medicine_id} Updated successfully')
            return redirect('inventory_add_code')
        else:
            addfees= Code_medicine.objects.all()
            return render(request,"inventory/add_code.html",{'form1':form1,'err':True,'object':object,'addfees':addfees})
    else:
        form=CodeForm()
        return render(request,"inventory/add_code.html",{'form':form})


@login_required(login_url='login_view')
def delete_code(request):
    id= request.POST.get('newobid')
    x = Code_medicine.objects.get(id=id)
    name=x.medicine_id
    x.delete()
    messages.success(request, f'{name} deleted successfully')
    return redirect('inventory_add_code')


# add_medicine
@login_required(login_url='login_view')
def add_medicine(request):
    fees=Code_medicine.objects.all()
    if request.method == 'POST':
        selected=request.POST.get('code')
        selected_code=Code_medicine.objects.get(id=selected)

        form = MedicineForm(request.POST)
        if form.is_valid():
            x=form.save()
            x.medicine_id=selected_code.medicine_id
            x.save()
            messages.success(request, 'medicine added successfully')
            form = MedicineForm()
            return render(request,'inventory/add_medicine.html', {'fees':fees,'add':True,'form': form,'medicine':incrementid()})
        else:
            return render(request,'inventory/add_medicine.html', {'selected_code':selected_code,'fees':fees,'add':True,'form': form,'medicine':incrementid()})
    else:
        form = MedicineForm()
        return render(request,'inventory/add_medicine.html', {'fees':fees,'add':True,'form': form,'medicine':incrementid()})


# search_medicine
@login_required(login_url='login_view')
def search_medicine(request):
    if request.method == 'POST':
        name_id=request.POST.get('search')
        start_date=request.POST.get('start_date')
        print(start_date)
        end_date=request.POST.get('end_date')
        medi=[i for i in Medicine.objects.filter(Q(medicine_name__iexact=name_id)|Q(medicine_id__iexact=name_id)) if i.quantity >0]
        medi_id=[i.id for i in medi] 
        try:
            a = datetime.datetime.strptime( start_date, '%Y-%m-%d').date()
            b = datetime.datetime.strptime( end_date, '%Y-%m-%d').date()
            medicines=Medicine.objects.filter(created_at__date__gte=a,created_at__date__lte=b,is_active=False)
            # medicines=[i for i in medicines if i.quantity > 0]
        except:
            a=start_date
            b=end_date
            medicines=[]
        if medi_id and medicines:
            medicines=[i for i in medicines if i.id in medi_id and i.quantity > 0 and i.is_active==False ]
        elif medi:
            medicines=medi
        else:
            medicines = medicines

        return render(request,'inventory/search_medicine.html', {'search':True,'medicines': medicines,'name_id':name_id,'start_date':start_date,'end_date':end_date})
    else:

        return render(request,'inventory/search_medicine.html', {'search':True})


# update_medicine
@login_required(login_url='login_view')
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
                medicines=Medicine.objects.filter(created_at__date__gte=a,created_at__date__lte=b,is_active=False)
            except:
                a=start_date
                b=end_date
                medicines=[]
            if medi_id and medicines:
                medicines=[i for i in medicines if i.id in medi_id  and i.is_active==False ]
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
                medicines=Medicine.objects.filter(created_at__date__gte=a,created_at__date__lte=b,is_active=False)
            except:
                a=start_date
                b=end_date
                medicines=[]
            if medi_id and medicines:
                medicines=[i for i in medicines if i.id in medi_id and i.is_active==False ]
            elif medi:
                medicines=medi
            else:
                medicines = medicines
            return render(request,'inventory/search_medicine.html', {'search':True,'object':id,'err':True,'form':form,'medicines': medicines,'name_id':name_id,'start_date':start_date,'end_date':end_date})

    else:
        
        return redirect('inventory_search_medicine')


@login_required(login_url='login_view')
def doctor(request):
    if request.method == "POST": 
        data = json.loads(request.body)
        print(data)
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
            evening=i['Evening'],night=i['Night'],days=i['Days'],total=i['Total'])

        for i in labtesting:
            Lab_test.objects.create(patient_id=patient_object,vitals_id=vital_object,lab_test=i['Tests'])


        Symptom.objects.create(patient_id=patient_object,vitals_id=vital_object,symptom=data['patient_symptom'] ,diagnose=data['patient_diagnose'])

        today_patient=data['today_patient']
        today=TodayPatients.objects.get(id=today_patient)
        today.is_consulted=True
        today.save()
        current_vital=GeneralVitals_new.objects.get(id=vital_object)
        current_vital.is_consulted=True
        current_vital.save()
        
        data={}
        return JsonResponse(data)
   

@login_required(login_url='login_view')
def medicine_amount(request):
    if request.method == "POST": 
        id = request.POST.get('consultingName')
        amount=AddFees.objects.get(id=id)
        amount=amount.amount
        data ={'data':amount}
        return JsonResponse(data)


@login_required(login_url='login_view')
def patients(request):
    if request.method == "POST": 
        id = request.POST.get('name')
        data ={}
        return JsonResponse(data)
    else:
        x= TodayPatients.objects.filter(created_at__contains=datetime.datetime.today().date(),is_consulted=True).order_by('-id')
        return render(request,'inventory/patients.html',{'x':x})



@login_required(login_url='login_view')
def medicine_quantity(request):
    if request.method == "POST":
        medicine_name = request.POST.get('medicineName')
        print(medicine_name)
        code=Medicine.objects.filter(medicine_name=medicine_name,is_active=False)
        try:
            min_quantity=code.last().code.min_quantity
        except:
            min_quantity=20
            
        code=  Medicine.objects.filter(medicine_name=medicine_name,is_active=False).aggregate(Sum('quantity')).get('quantity__sum')
        
        print(code)
        if code:
            if code < min_quantity:
                
                data={
                    'quantity':code
                } 
                return JsonResponse(data)
            else:
                data = {
                    'value':'none'
                }
                return JsonResponse(data)
        else:
                data = {
                    'value':'none'
                }
                return JsonResponse(data)
            
    

@login_required(login_url='login_view')
def lab_test(request,id,printer=None):
    prescription=TodayPatients.objects.get(id=id)
    lab=Lab_test.objects.filter(vitals_id=prescription.vitals_id)
    if printer:
        return render(request,'inventory/lab_test_print.html',{'prescription':prescription,'lab_test':lab})

    else:
        return render(request,'inventory/lab_test.html',{'prescription':prescription,'lab_test':lab})


@login_required(login_url='login_view')
def consult_fees(request,id,printer=None):
    
    prescription=TodayPatients.objects.get(id=id)
    
    lab=Fees.objects.filter(vitals_id=prescription.vitals_id)
    if printer:
        return render(request,'inventory/consult_fees_print.html',{'prescription':prescription,'lab_test':lab})

    else:
        return render(request,'inventory/consult_fees.html',{'prescription':prescription,'lab_test':lab})


@login_required(login_url='login_view')
def out_medicine(request,id,printer=None):
    prescription=TodayPatients.objects.get(id=id)
    tablet= Patient_medicine.objects.filter(vitals_id=prescription.vitals_id,is_delivered=False)
    if printer:
        return render(request,'inventory/out_medicine_print.html',{'prescription':prescription,'tablet':tablet})

    else:
        return render(request,'inventory/out_medicine.html',{'prescription':prescription,'tablet':tablet})

def prescription(request,id):
    prescription=TodayPatients.objects.get(id=id)
    tablet=Patient_medicine.objects.filter(vitals_id=prescription.vitals_id)
    if request.method == "POST": 
        id_list = request.POST.get('id')
        x = id_list.split(",")
        for i in x:
            try:
                patients=Patient_medicine.objects.get(id=i)
                prescription.is_seperated=True
                patients.is_delivered=True
                patients.save()
                prescription.save()
                count=int(patients.total)
                name=patients.medicine_name
                if count == 0:
                    count=1
                    stock(name,count)
                else:
                    stock(name,count)

               


            except:
                print("hi")


        table=Patient_medicine.objects.filter(vitals_id=prescription.vitals_id,is_delivered=True)
        name=[i.medicine_name for i in table]

        amount=[]
        for i in name:
            medi=Medicine.objects.filter(medicine_name=i,is_active=False)
            price=[]
            for j in medi:
                price.append(j.medicine_price)
            amount.append(max(price))
        
                
        tablet=zip(table,amount)
        total=[]
        for i,j in tablet:
            if float(i.total) > 0:
                total.append(float(i.total)*float(j))
            else:
                total.append(float(j))

        
        total_amount=sum(total)
        print(total_amount)
        medicine_total_amount.objects.create(patient_id=prescription.patient_id,vitals_id=prescription.vitals_id,medicine_total_amount=total_amount)
        return redirect('inventory_patients') 
    else:       
        return render(request,'inventory/prescription.html',{'tablet':tablet})




def medicine_bill(request,id,printer=None):
    
    prescription=TodayPatients.objects.get(id=id)
    table=Patient_medicine.objects.filter(vitals_id=prescription.vitals_id,is_delivered=True)
    name=[i.medicine_name for i in table]

    amount=[]
    for i in name:
        medi=Medicine.objects.filter(medicine_name=i,is_active=False)
        price=[]
        for j in medi:
            price.append(j.medicine_price)
        amount.append(max(price))
    
            
    tablet=zip(table,amount)
    total=[]
    for i,j in tablet:
        if float(i.total) > 0:
            total.append(float(i.total)*float(j))
        else:
            total.append(float(j))

    total_tablet= zip(table,amount,total)
    total_amount=sum(total)
    print(total_amount)
    # medicine_total_amount.objects.create(patient_id=prescription.patient_id,vitals_id=prescription.vitals_id,medicine_total_amount=total_amount)

    if printer:
        return render(request,'inventory/medicine_bill_print.html',{'total_amount':total_amount,'prescription':prescription,'tablet':total_tablet})

    else:

        return render(request,'inventory/medicine_bill.html',{'total_amount':total_amount,'prescription':prescription,'tablet':total_tablet})


def add_medicine_code(request):
    if request.method == "POST":
        id = request.POST.get('consultingName')
        print(id)
        code=Code_medicine.objects.get(id=id)
        data={
            'medicine_name':code.medicine_name,
            'medicine_brand':code.medicine_brand
        } 
        return JsonResponse(data)


def incrementid():
    last = Medicine.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "MD022" "%04d" % last)

def stock(name,count):
    medicine=Medicine.objects.filter(medicine_name=name,is_active=False).first()
    medicine_count=medicine.quantity
    diff=medicine_count - count
    if diff > 0:
        medicine.quantity=medicine.quantity - count 
        medicine.save()
    elif diff == 0:
        medicine.quantity=medicine.quantity - count 
        medicine.is_active=True
        medicine.save()
    else:
        medicine_count=medicine.quantity
        neg_diff=count - medicine_count
        medicine.quantity=medicine.quantity - medicine_count
        medicine.is_active=True
        medicine.save()
        if neg_diff > 0:
            stock(medicine.medicine_name,neg_diff)



def code(medicine_name):
    code=  Medicine.objects.filter(medicine_name=medicine_name,is_active=False).aggregate(Sum('quantity')).get('quantity__sum')
    return code 

print(code('Tablet'))