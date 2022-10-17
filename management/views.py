from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import BillsModel, ProductDetails,PatientDetails,TodayPatients,PrescribedMedicine,HealthHistory,BillsModel
from .forms import RegisterForm, InputForm,ProductDetailsForm,PatientDetailsForm,HistoryForm,MedicineDetailForm,BillsModelForm,GeneralVitalsForm
from django.contrib.auth import login as log
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib import messages
from datetime import date

import datetime
from django.contrib.auth.decorators import login_required
from django.db.models import Q



#user views
def navbar(request):
    return render(request,"management/navbar.html")


def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        
        # is_user=request.POST.get("is_user")
        # if is_user==None:
        #     is_user=0
        # is_admin=request.POST.get("is_admin")
        # if is_admin==None:
        #     is_admin=0
         
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
            print(form.errors)
            return render(request,'management/register.html', {'form':form})             
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
                    return redirect('user_view')
                elif user.is_customer:
                    log(request,user)
                    return redirect('patient_register')
                else:
                    return HttpResponse("invalid")                  
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
    return redirect('register')



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
        print(selected_date)
        date_time_obj = datetime.datetime.strptime( selected_date, '%Y-%m-%d').date()
        print( date_time_obj)
        result= ProductDetails.objects.filter(created_at__date__gte= date_time_obj)
        print(result)        
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
            # edit.product_name = request.POST.get("product_name")
            # edit.product_id = request.POST.get("product_id")
            # edit.product_quantity= request.POST.get("product_quantity")
            # edit.product_price = request.POST.get("product_price")
            # date=request.POST.get("date")
            # print('hi')
            # print(str(date))
            # if date=='':
            #     edit.expiry_date=request.POST.get("expiry_date")
            # else:
            #     edit.expiry_date=date

            # edit.save()    
            # print(edit)
        
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


def patients_register(request):
    if request.method=="POST":
        patient_id=request.POST.get("patient_id")
        print(patient_id)
        form = PatientDetailsForm(request.POST)        
        if form.is_valid(): 
            form.save()             
            messages.success(request, 'Details created successfully') 
            return redirect('search_patient')
        else:
            print(form.errors)            
            messages.info(request,'User Registration Failed')
            return render(request,'management/patient_register.html',{'patient_id':increment_patient_id(),'form': form})     
    else:
     form = PatientDetailsForm()  
     print(form.errors) 
     return render(request,'management/patient_register.html',{'patient_id':increment_patient_id(),'form':form})  



def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def increment_patient_id():
    last = PatientDetails.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "DB022" "%03d" % last)


def search_patient(request):
    x=  PatientDetails.objects.all()
    if request.method=="POST": 
        patient_id=request.POST.get("patient_id") 
        patient_name=request.POST.get("patient_name") 
        phone_number=request.POST.get("phone_number")
        try:
            result=PatientDetails.objects.filter(phone_number=phone_number)
            return render(request,'management/search_patient.html',{'x':result,'phone_number':phone_number}) 
        except:
               result= PatientDetails.objects.filter(Q(patient_name=patient_name)|Q(patient_id=patient_id))
               
                
        return render(request,'management/search_patient.html',{'x':result,'patient_name':patient_name,'patient_id':patient_id})             
        
    else:   
        y=  TodayPatients.objects.filter(created_at__contains=datetime.datetime.today().date())  
        y =[i.patient.patient_id for i in y]   
        print(y)
        return render(request,'management/search_patient.html',{'x':x})  

def click_patient(request,id):
    patient=PatientDetails.objects.get(id=id)
    x=  PatientDetails.objects.filter(id=patient.id)
    
    
    return render(request,"management/search_patient.html",{'patient':patient,'x':x,})


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




def add_patient(request):
    if request.method=="POST": 
        id=request.POST.get("patient_id")
        print(id)
        add_patient = PatientDetails.objects.get(patient_id=id)
        print(add_patient)    

        TodayPatients.objects.create(patient=add_patient)
        return redirect('search_patient')

def user_view(request):
    x=  TodayPatients.objects.filter(created_at__contains=datetime.datetime.today().date())
    return render(request,"management/user_view.html",{'x':x})

def doctor_view(request):
    x=  TodayPatients.objects.filter(created_at__contains=datetime.datetime.today().date())
    return render(request,"management/doctor_view.html",{'x':x})

def disable_view(request,id):
     disable=TodayPatients.objects.get(id=id)
     print(disable)
     disable.is_active=False
     disable.save()    

     return redirect('user_view')



def enable_view(request,id):
     enable=TodayPatients.objects.get(id=id)    
     enable.is_active=True
     enable.save()
     return redirect('user_view')

def general_vitals(request):    
    if request.method=="POST":
        id=request.POST.get("object_id")        

        general=TodayPatients.objects.get(patient=id)
        patient_id=general.patient_id
        print(patient_id)   
        
        form=GeneralVitalsForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('user_view')
        else:
            x=  TodayPatients.objects.filter(created_at__contains=datetime.datetime.today().date())
            
            return render(request,"management/user_view.html",{'form':form,'x':x}) 

    else:
        form=GeneralVitalsForm()
        print(form.errors)
        return render(request,"management/user_view.html",{'form':form})
    


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

# def update(request,id):
#     return render("management/update.html")
    





    




    

  





     
    
    



   



            


