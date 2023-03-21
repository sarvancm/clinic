from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import BillsModel, GeneralVitals_new, ProductDetails,PatientDetails,TodayPatients,PrescribedMedicine,HealthHistory,BillsModel,AddFees
from .forms import RegisterForm, InputForm,ProductDetailsForm,PatientDetailsForm,HistoryForm,MedicineDetailForm,BillsModelForm,GeneralVitals_newForm,AddFeesForm
from django.contrib.auth import login as log
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from dateutil import relativedelta
from inventory.models import Medicine,Allergy_Medicine,Patient_medicine,Symptom,Lab_test,Code_medicine,medicine_total_amount,Fees
import calendar
from django.db.models import Sum
from .decorators import *
from datetime import datetime,timedelta,date,time



#dashboard
@login_required(login_url='login_view')
@customer_not
def dashboard(request):
     
    month=datetime.now().month
    year=datetime.now().year
    month_start = date(year, month, 1)
    month_end =date(year, month, calendar.monthrange(year, month)[1])
    monthly_patient = len(TodayPatients.objects.filter(created_at__date__gte=month_start,created_at__date__lte=month_end,is_consulted=True))
    today_patient=  len( TodayPatients.objects.filter(created_at__contains=datetime.today().date(),is_consulted=True))
    monthly_medicine_amount = medicine_total_amount.objects.filter(created_at__date__gte=month_start,created_at__date__lte=month_end).aggregate(Sum('medicine_total_amount')).get('medicine_total_amount__sum')
    today_medicine_amount=  medicine_total_amount.objects.filter(created_at__contains=datetime.today().date()).aggregate(Sum('medicine_total_amount')).get('medicine_total_amount__sum')
    if today_medicine_amount==None:
        today_medicine_amount=0
    if monthly_medicine_amount==None:
        monthly_medicine_amount=0
    monthly_fees = Fees.objects.filter(created_at__date__gte=month_start,created_at__date__lte=month_end).aggregate(Sum('fees_amount')).get('fees_amount__sum')
    today_fees=  Fees.objects.filter(created_at__contains=datetime.today().date()).aggregate(Sum('fees_amount')).get('fees_amount__sum')
    if monthly_fees==None:
        monthly_fees=0
    if today_fees==None:
        today_fees=0
    week_start=datetime.now() - timedelta(days=((datetime.now().weekday() + 1) % 7))
    week_end=week_start+timedelta(days=6)
    weekly_patient=len(TodayPatients.objects.filter(created_at__date__gte=week_start.date(),created_at__date__lte=week_end.date(),is_consulted=True))
    weekly_medicine_amount = medicine_total_amount.objects.filter(created_at__date__gte=week_start.date(),created_at__date__lte=week_end.date()).aggregate(Sum('medicine_total_amount')).get('medicine_total_amount__sum')
    weekly_fees = Fees.objects.filter(created_at__date__gte=week_start.date(),created_at__date__lte=week_end.date()).aggregate(Sum('fees_amount')).get('fees_amount__sum')
    if weekly_medicine_amount == None:
        weekly_medicine_amount=0
    if weekly_fees == None:
        weekly_fees=0
    total_patient=len(PatientDetails.objects.all())
    medicines=[i for i in Code_medicine.objects.all() if i.total_quantity() < i.min_quantity]
    
    return render(request,'management/dashboard.html', {
        'medicines':medicines,
        'total_patient':total_patient,
        'weekly_income':weekly_medicine_amount+weekly_fees,
        'weekly_patient':weekly_patient,
        'monthly_income':monthly_fees+monthly_medicine_amount,
        'daily_income':today_medicine_amount+today_fees,
        'monthly_patient':monthly_patient,
        'today_patient':today_patient,
        'dash':True
        })


#navbar
@login_required(login_url='login_view')
def navbar(request):
    user=request.user                                        
  
    return render(request,"management/navbar.html",{'user':user})

#user views
@login_required(login_url='login_view')
def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        user_select=request.POST.get("user_select")
        if form.is_valid():  
            x=form.save() 
            user_select=request.POST.get("user_select")
            if user_select=="admin":
                x.is_admin=1
                x.save()
            else:
                x.is_user=1
                x.save()       
        
            
            messages.success(request, 'Account created successfully') 
            return redirect('login_view')
        else:
            return render(request,'management/register.html', {'user_select':user_select,'form':form})             
    else:        
        
        return render(request, 'management/register.html') 


def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST) 
        if form.is_valid():
            username=form.cleaned_data.get('username')            
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)            
            if user:    
                if user.is_admin :
                    log(request,user)
                    messages.success(request, f'Welcome {username}') 
                    return redirect('doctor_view')
                elif user.is_user:
                    log(request,user)
                    messages.success(request, f'Welcome {username}') 
                    return redirect('user_view')
                else:
                    log(request,user)
                    messages.success(request, f'Welcome {username}') 
                    return redirect('dashboard')                  
            else:
                messages.error(request,'Not user')    
                return render(request,'management/login.html',{'form':form})          
        else:
            print(form.errors)
            return render(request,'management/login.html',{'form':form})     
    else:      
        form=AuthenticationForm()
        return render(request,'management/login.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.success(request, 'logout successfully') 
    return redirect('login_view')



# product views

def create_product_details(request):
    
    if request.method=="POST":
        form = ProductDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'created successfully') 
            return redirect('list_product_details')
        else:
            form = ProductDetailsForm()
            return render(request,'management/create_product_details.html',{'form':form})         
       
    else:
        form = ProductDetailsForm()
        return render(request,'management/create_product_details.html',{'form':form})



def list_product_details(request):
    x=  ProductDetails.objects.all()
   
    if request.method=="POST": 
        selected_date=request.POST.get("date") 
        date_time_obj = datetime.datetime.strptime( selected_date, '%Y-%m-%d').date()
        result= ProductDetails.objects.filter(created_at__date__gte= date_time_obj)      
        return render(request,'management/list_product_details.html',{'x':result})
    else:
        
        return render(request,'management/list_product_details.html',{'x':x})


@login_required(login_url='login_view')
def view_product_details(request,id):
    if request.user.is_admin:
     x=  ProductDetails.objects.get(id=id)
     return render(request,'management/view_product_details.html',{'x':x})
    
    else:
        return HttpResponse('not permit')



def sale(request):
    if request.method=="POST":
        form=InputForm(request.POST)
        if form.is_valid():
            x=form.save()           
            y=x.items_saled            
            pro=ProductDetails.objects.get(id=x.item.id)
            pro.product_value=pro.product_value-y
            pro.save()         
        return redirect('view_product_details')
    else:
       form=InputForm()
       return render(request,'management/sale.html',{'form':form}) 


@login_required(login_url='login_view')
def edit_product_details(request,id):
    if request.user.is_admin:
        edit = ProductDetails.objects.get(id=id)
        if request.method=="POST":  
            form = ProductDetailsForm(instance =edit)
            return render(request,"management/view_product_details.html",{'edit':edit, 'form':form})
        else:
            form = ProductDetailsForm(instance =edit)
            return render(request,"management/edit_product_details.html",{'edit':edit, 'form':form})
    else:
        return HttpResponse('not permit')



def delete_product(request,id):
    x = ProductDetails.objects.get(id=id)
    x.delete()
    return redirect('list_product_details')


@login_required(login_url='login_view')
def enable_product_details(request,id):
    if request.user.is_admin:
        enable = ProductDetails.objects.get(id=id)
        enable.is_active=True
        enable.save()
        return redirect('list_product_details')        
   
    else:
        return HttpResponse('not permit')


@login_required(login_url='login_view')
def disable_product_details(request,id):
    if request.user.is_admin:
        disable=ProductDetails.objects.get(id=id)
        disable.is_active=False
        disable.save()
        return redirect('list_product_details')  
    else:
        return HttpResponse('not permit')  


# patient views

@login_required(login_url='login_view')
def patients_register(request):
    if request.method=="POST":
        age=request.POST.get("age")
        form = PatientDetailsForm(request.POST)
       
        if form.is_valid(): 
            form.save()           
            messages.success(request, 'Details created successfully')
            return redirect('search_patient')
        else:   
            messages.warning(request,'Patient Registration Failed')
            return render(request,'management/patient_register.html',{'age':age,'patient_id':increment_patient_id(),'form': form})     
    else:
     form = PatientDetailsForm()  
     
     return render(request,'management/patient_register.html',{'patient_id':increment_patient_id(),'form':form})  






def increment_patient_id():
    last = PatientDetails.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "DB022" "%03d" % last)

@login_required(login_url='login_view')
def search_patient(request):
    x=  PatientDetails.objects.all()
    if request.method=="POST": 
        patient_id=request.POST.get("patient_id") 
        
        result1 = PatientDetails.objects.filter(phone_number__iexact = patient_id)
        result2 = PatientDetails.objects.filter(patient_id__iexact = patient_id)
        if result1:
            result=result1
            
        elif result2:
            result=result2
            
        else:
            result=[]
          

        return render(request,'management/search_patient.html',{'x':result,'phone_number':patient_id})              
        
    else:   
        y=  TodayPatients.objects.filter(created_at__contains=datetime.today().date())  
        y =[i.patient.patient_id for i in y]   
        return render(request,'management/search_patient.html',{})  


@login_required(login_url='login_view')
def click_patient(request,id,name=None):
    patient_id=name
    result1 = PatientDetails.objects.filter(phone_number__iexact = patient_id)
    result2 = PatientDetails.objects.filter(patient_id__iexact = patient_id)
    if result1:
        result=result1
        
    elif result2:
        result=result2
        
    else:
        result=[]
    patient=PatientDetails.objects.get(id=id)
    
    
    
    return render(request,"management/search_patient.html",{'patient':patient,'x':result,'phone_number':name})



@login_required(login_url='login_view')
def update_patient_details(request):
        
    if request.method=="POST": 
         update = PatientDetails.objects.get(id=request.POST.get("ob"))
         update.patient_name=request.POST.get("patient_name")
         update.Address=request.POST.get("address")
         update.Age=request.POST.get("age")
         update.Phone_number=request.POST.get("phone_number")
         update.save() 

         return redirect('search_patient')        
    else:   
        return render(request,"management/search_patient.html")



@login_required(login_url='login_view')
def add_patient(request):
    if request.method=="POST": 
        id=request.POST.get("patient_id")
        add_patient = PatientDetails.objects.filter(patient_id=id).last() 
        if add_patient:
            TodayPatients.objects.create(patient=add_patient)
            messages.success(request, f'{add_patient.patient_name} registered to out patient list successfully')
            return redirect('search_patient')
        else:
            messages.warning(request, f'select the patient first')
            return redirect('search_patient')



@login_required(login_url='login_view')
def user_view(request):
    user=request.user
    x=  TodayPatients.objects.filter(created_at__contains=datetime.today().date()).order_by('-id')
    list=[]
    for i in x:
        try:
            y=GeneralVitals_new.objects.filter(patient_id=i.patient_id,created_at__contains=datetime.today().date()).last()   
        except:
            y=None
        list.append(y)
    
    z=zip(list,x)    
   
    return render(request,"management/user_view.html",{'x':x,'z':z,'user':user})


@login_required(login_url='login_view')
def doctor_view(request,id=None):
    
    if id :
         messages.success(request, 'consulting Details created successfully') 
    user=request.user
    if user.is_admin:
        x=  [TodayPatients.objects.get(id=i.id) for i in TodayPatients.objects.filter(created_at__contains=datetime.today().date(),is_active=True) ]
        x.reverse()


        return render(request,"management/doctor_view.html",{'x':x,'user':user})
    else:
        messages.success(request,"Not admin")
        return redirect('login_view')



@login_required(login_url='login_view') 
def doctor_vie(request,id):  
    fees= [i for i in AddFees.objects.all() if i.fee_name != 'Consultation Fee']
    Consultation = AddFees.objects.filter(fee_name='Consultation Fee')
    today_patient=  TodayPatients.objects.get(id=id)
    view=today_patient.patient_id
    vitals_id= today_patient.vitals_id
    y=PatientDetails.objects.filter(id=today_patient.patient_id).first()
    z=GeneralVitals_new.objects.filter(id=vitals_id).first()
    medicines= Code_medicine.objects.all() 
    allergy_id=[i.id for i in GeneralVitals_new.objects.filter(patient_id=y.id)]
    try:
        allergy_id=allergy_id[-2]
        return_allergy=[i.medicine_name for i in Allergy_Medicine.objects.filter(patient_id=y.id,vitals_id=allergy_id)]
    except:
        return_allergy=[]

    total_vitals=GeneralVitals_new.objects.filter(patient_id=view,is_consulted=True).order_by('id')

    if total_vitals:
        total_vitals=list(total_vitals)
        recent=total_vitals[-1].id
    else:
        recent=2
    Patient_medicine_list=[]
    symptom_list=[]
    lab_list=[]
    forward=[]
    backward=[0] 
    count=1
    for i in total_vitals:
        medicine=Patient_medicine.objects.filter(patient_id=view,vitals_id=i.id)
        symptom=Symptom.objects.filter(patient_id=view,vitals_id=i.id)
        lab=Lab_test.objects.filter(patient_id=view,vitals_id=i.id)
        if count>1:
            forward.append(i)

        backward.append(i)
        Patient_medicine_list.append(medicine)
        symptom_list.append(symptom)
        lab_list.append(lab)
        count += 1

    forward.append(0)
    backward.pop(-1)

    history=zip(total_vitals,lab_list,symptom_list,Patient_medicine_list,forward,backward) 

    return render(request,"management/doctor_vie.html",{'Consultation':Consultation,'recent':recent,'today_patient':today_patient,'history':history,'x':y,'z':z,'fees':fees,'medicines':medicines,'return_allergy':return_allergy})
    

@login_required(login_url='login_view')
def disable_view(request,id):
     disable=TodayPatients.objects.get(id=id)
     disable.is_active=False
     disable.save()    
     messages.success(request, f'{disable.patient.patient_name} removed from doctor view successfully') 
     return redirect('user_view')


@login_required(login_url='login_view')
def enable_view(request,id):
     enable=TodayPatients.objects.get(id=id)    
     enable.is_active=True
     enable.save()
     messages.success(request, f'{enable.patient.patient_name} added to doctor view successfully') 
     return redirect('user_view')


@login_required(login_url='login_view')
def general_vitals(request):   
    if request.method=="POST":
        id=request.POST.get("object")
        vitalsid=request.POST.get("vitals")  
        general=TodayPatients.objects.get(id=id)
        try:
           vital=GeneralVitals_new.objects.get(id=vitalsid)
        except:
            vital=[]

        if vital:
            form=GeneralVitals_newForm(request.POST)
            vital.temperature=request.POST.get("temperature")
            vital.pulse_rate=request.POST.get("pulse_rate")
            vital.blood_pressure_start=request.POST.get("blood_pressure_start")
            vital.blood_pressure_end=request.POST.get("blood_pressure_end")
            vital.height=request.POST.get("height")
            vital.weight=request.POST.get("weight")
            vital.others=request.POST.get("others")
            if form.is_valid():
                vital.save()
                messages.success(request, f'vitals for {general.patient.patient_name} updated successfully')            
                return redirect('user_view')
            else:
                id=request.POST.get("object")
                vitalsid=request.POST.get("vitals") 
                x=  TodayPatients.objects.filter(created_at__contains=datetime.today().date())
                print(x)
                list=[]
                for i in x:
                    try:
                        y=GeneralVitals_new.objects.filter(patient_id=i.patient_id,created_at__contains=datetime.today().date()).last()   
                    except:
                        y=None
                    list.append(y)
                
                z=zip(list,x)              
                return render(request,"management/user_view.html",{'form':form,'err':True,'x':x,'z':z,'object':id,'vital':vitalsid}) 

            

        else:
            
            patient_id=general.patient_id      
            form=GeneralVitals_newForm(request.POST)
            if form.is_valid():
                x=form.save()
                x.patient_id=patient_id
                x.save()
                general.vitals_id=x.id
                general.is_vital=True
                general.is_active=True
                general.save()          
                messages.success(request, f'vitals for {general.patient.patient_name} created successfully')            
                return redirect('user_view')
            else:
                x=  TodayPatients.objects.filter(created_at__contains=datetime.today().date())
                print(x)
                list=[]
                for i in x:
                    try:
                        y=GeneralVitals_new.objects.filter(patient_id=i.patient_id,created_at__contains=datetime.today().date()).last()   
                    except:
                        y=None
                    list.append(y)
                
                z=zip(list,x)              
                return render(request,"management/user_view.html",{'form':form,'patient_id':patient_id,'err':True,'x':x,'z':z,'object':id,'vital':vitalsid}) 

    else:
        form=GeneralVitals_newForm()
        x=  TodayPatients.objects.filter(created_at__contains=datetime.today().date())
        return render(request,"management/user_view.html",{'form':form,'x':x})
    


def add_new_history(request,id):
    if request.method=="POST":
        form=HistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_view')
        else:
             return render(request,"management/add_new_history.html",{'form':form})       
    else:
        form=HistoryForm()
        return render(request,"management/add_new_history.html",{'form':form})


def medicine_details(request,id):
    medicine_detail=TodayPatients.objects.get(id=id)
    disable_view=TodayPatients.objects.get(id=id)
    disable_view.is_active=True
    disable_view.save()   
    if request.method=="POST":
        form=MedicineDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_view')
        else:
            print(form.errors)
            return redirect('user_view')
    else:
        form=MedicineDetailForm()
        return render(request,"management/medicine_details.html",{'medicine_detail':medicine_detail})



def past_history(request,id):
   
    past_detail=TodayPatients.objects.get(id=id)
    x=PrescribedMedicine.objects.filter(patient_id=past_detail.patient.id)  
    return render(request,"management/past_history.html",{'past_detail':past_detail,'x':x})


def bills(request,id):
    bill_detail=PatientDetails.objects.get(id=id)
    past_detail=TodayPatients.objects.filter(patient_id=id).last()    
    x=PrescribedMedicine.objects.filter(patient_id=id).last() 
    if request.method=="POST":
        form=BillsModelForm(request.POST)
        if form.is_valid():
            x=form.save()
            x.bill_no=increment_bill_no()
            x.save()
            return redirect('search_patient')

        else:
            form=BillsModelForm()
            print(form.errors)
            return render(request,"management/bills.html",{'form':form})

    form=BillsModelForm()
    return render(request,"management/bills.html",{'bill_no':increment_bill_no(),'bill_detail':bill_detail,'x':x,'past_detail': past_detail,'form':form})

def edit_bills(request,id):
    edit_bills=BillsModel.objects.get(id=id)
    form=BillsModelForm(instance=edit_bills)
    if request.method=="POST":
        form=BillsModelForm(request.POST,instance=edit_bills)
        if form.is_valid():
            edit=form.save()
            edit.save()
            return redirect('search_patient')  
        else:
            print(form.errors)
            return render(request,"management/edit_bills.html",{'edit_bills':edit_bills,'form':form})
    else:
        
        return render(request,"management/edit_bills.html",{'edit_bills':edit_bills,'form':form})

def increment_bill_no():
    last = BillsModel.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "BBILL001" "%03d" % last)


@login_required(login_url='login_view')
def add_fees(request):
    addfees= AddFees.objects.all()    
    if request.method=="POST":
        amount=request.POST.get('amount')
        form=AddFeesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'created successfully')
            return redirect('add_fees') 
        else:
            return render(request,"management/add_fees.html",{'addfees':addfees,'form':form}) 
    else:
        form=AddFeesForm()
        return render(request,"management/add_fees.html",{'addfees':addfees,'form':form})


@login_required(login_url='login_view')
def fee_mode(request):
    if request.method=="POST":
        object=request.POST.get("ob")
        name=request.POST.get("fee_name")
        amount=request.POST.get("amount")
        z=AddFees.objects.get(id=object)
        form1=AddFeesForm(request.POST,instance=z)          
        if form1.is_valid():
            z.fee_name= name
            z.amount=  amount 
            z.save()   
            messages.success(request, 'Updated successfully')
            return redirect('add_fees')
        else:
            addfees= AddFees.objects.all()
            return render(request,"management/add_fees.html",{'form1':form1,'err':True,'object':object,'addfees':addfees})
    else:
        form=AddFeesForm()
        return render(request,"management/add_fees.html",{'form':form})


@login_required(login_url='login_view')
def delete_fees(request):
    id= request.POST.get('newobid')
    x = AddFees.objects.get(id=id)
    name=x.fee_name
    x.delete()
    messages.success(request, f'{name} deleted successfully')
    return redirect('add_fees')

    
@login_required(login_url='login_view')
def report(request):
    month=datetime.now().month-1
    year=datetime.now().year
    month_start = date(year, month, 1)
    month_end =date(year, month, calendar.monthrange(year, month)[1])
    monthly_patient = TodayPatients.objects.filter(created_at__date__gte=month_start,created_at__date__lte=month_end,is_consulted=True)
    monthly_patient_fees=[sum(i.fees_amount for i in Fees.objects.filter(vitals=j.vitals)) for j in monthly_patient]
    monthly_patient_medicine=[sum(i.medicine_total_amount for i in medicine_total_amount.objects.filter(vitals=j.vitals)) for j in monthly_patient]
    total=[i+j for i,j in zip(monthly_patient_fees,monthly_patient_medicine)]
    today_patient=  TodayPatients.objects.filter(created_at__contains=datetime.today().date(),is_consulted=True)
    monthly_medicine_amount = medicine_total_amount.objects.filter(created_at__date__gte=month_start,created_at__date__lte=month_end).aggregate(Sum('medicine_total_amount')).get('medicine_total_amount__sum')
    today_medicine_amount=  medicine_total_amount.objects.filter(created_at__contains=datetime.today().date()).aggregate(Sum('medicine_total_amount')).get('medicine_total_amount__sum')
    if today_medicine_amount==None:
        today_medicine_amount=0
    if monthly_medicine_amount==None:
        monthly_medicine_amount=0
    
    monthly_fees = Fees.objects.filter(created_at__date__gte=month_start,created_at__date__lte=month_end).aggregate(Sum('fees_amount')).get('fees_amount__sum')
    today_fees=  Fees.objects.filter(created_at__contains=datetime.today().date()).aggregate(Sum('fees_amount')).get('fees_amount__sum')
    if monthly_fees==None:
        monthly_fees=0
    if today_fees==None:
        today_fees=0
    today_income= today_fees +today_medicine_amount
    monthly_income= monthly_fees +monthly_medicine_amount
    monthly_patient_zip=zip(monthly_patient,monthly_patient_fees,monthly_patient_medicine,total)
    return render(request,"management/report.html",locals())





    




    

  





     
    
    



   



            


