from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import Medicine
import datetime
from django.db.models import Q

# Create your views here.

# add_medicine
def add_medicine(request):

    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'medicine added successfully')
            form = MedicineForm()
            return render(request,'inventory/add_medicine.html', {'form': form,'medicine':incrementid()})
        else:
            return render(request,'inventory/add_medicine.html', {'form': form,'medicine':incrementid()})
    else:
        form = MedicineForm()
    return render(request,'inventory/add_medicine.html', {'form': form,'medicine':incrementid()})


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

        return render(request,'inventory/search_medicine.html', {'medicines': medicines,'name_id':name_id,'start_date':start_date,'end_date':end_date})
    else:

        return render(request,'inventory/search_medicine.html', {})


# update_medicine
def update_medicine(request):

    if request.method == 'POST':
        id = request.POST.get('object_id')
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
        object=Medicine.objects.get(id=id)
        form = MedicineForm(request.POST,instance=object)
        if form.is_valid():
            form.save()
            messages.success(request, 'medicine updated successfully')
            
            return render(request,'inventory/search_medicine.html', {'medicines': medicines,'name_id':name_id,'start_date':start_date,'end_date':end_date})

        else:
            print(form.errors)
            return render(request,'inventory/search_medicine.html', {'object':id,'err':True,'form':form,'medicines': medicines,'name_id':name_id,'start_date':start_date,'end_date':end_date})

    else:
        
        return redirect('inventory_search_medicine')



def incrementid():
    last = Medicine.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "MD022" "%04d" % last)