from django.shortcuts import render, HttpResponse
from .models import vehicle,vehicle_type
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.html')

def All_Vehicle(request):
    Veh=vehicle.objects.all()
    context={

        'Vehicle':vehicle
    }
    print(context)
    return render(request,'View_All_Vehicle.html',context)

def Add_Vehicle(request):
    if request.method=='POST':
        vehicle_no=(request.POST['vehicle_no'])
        vehicle_type=(request.POST['vehicle_type'])
        vehicle_model = (request.POST['vehicle_model'])
        vehicle_description = (request.POST['vehicle_description'])

        new_Vehicle=vehicle(vehicle_no=vehicle_no,vehicle_type=vehicle_type,vehicle_model=vehicle_model,vehicle_description=vehicle_description)
        new_Vehicle.save()

        return HttpResponse('Vehicle added successfully')
    elif request.method=='GET':
        return render(request,'Add_Vehicle.html')
    else:
        return HttpResponse('An Exception Occured! Vehicle has not been added')



def Remove_Vehicle(request,Vehicle_id=0):
    if Vehicle_id:
        try:
            Vehicle_to_be_Removed=vehicle.object.get(id=Vehicle_id)
            Vehicle_to_be_Removed.delete()

        except:
            return HttpResponse("Vehicle Removed successfully")

    Vehicles=vehicle.objects.all()
    context={
        'Vehicle':vehicle

    }


    return render(request,'remove_vehicle.html',context)


class vehicle:
    pass


def Filter_vehicle(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        Vehicle=vehicle.objects.all()
        if Vehicle_no:
            Vehicle=vehicle.filter(vehicle_no=Vehicle_no)
        if Vehicle_type:
            Vehicle=vehicle.filter(vehicle_type__=Vehicle_type)
        if Vehicle_model:
            vehicle=Vehicle.filter(model__name=vehicle_model)

        context={
            'vehicle':Vehicle
        }

        return render(request,'View_all_Vehicles', context)
    elif request.method=='GET':
        return render(request,'Filter_Vehicles.html')
    else:
        return HttpResponse('error')
