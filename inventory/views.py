from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import MedicineForm
from .models import Medicine

# Create your views here.


def add_medicine(request):

    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'expencess added successfully')
            return render(request,'inventory/add_medicine.html', {'form': form,'medicine':incrementid()})
        else:
            return render(request,'inventory/add_medicine.html', {'form': form,'medicine':incrementid()})
    else:
        form = MedicineForm()
    return render(request,'inventory/add_medicine.html', {'form': form,'medicine':incrementid()})







def incrementid():
    last = Medicine.objects.last()
    if last == None:
        last = 0
    else:
        last = last.id
    last+=1
    return ( "MD022" "%04d" % last)