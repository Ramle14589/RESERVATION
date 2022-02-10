from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import context
from django.urls import is_valid_path
# Create your views here.


from .forms import ClientForm
from .forms import PlanningForm
from .forms import ReservationForm

from .models import *



def main(request):
    return render(request ,'chambre\main.html')   

def Clients(request,pk):
    Clients=Client.objects.get(id=pk)
    Reservations=Clients.reservation_set.all()
    nomb_reservation= Reservations.count()
    Plannings=Clients.planning_set.all()
    context={'Clients':Clients ,'Reservations':Reservations ,'Plannings':Plannings,'nomb_reservation':nomb_reservation}
    return render( request ,'chambre\Clients.html',context)


def Plannings(request):
    Clients=Client.objects.all()
    Reservationss=Reservation.objects.all()
    t_Clients=Clients.count()
    context={'Client':Clients ,'t_Clients':t_Clients,'Reservation':Reservationss}
    return render(request ,'chambre\Plannings.html' ,context)

def Reservations(request):
    """ Reservations=Reservation.objects.get(id=pk)
    chambre=Chambre.reservation_set.all()
    context={'Reservations':Reservations ,'chambre':chambre } """
    return render(request ,'chambre\Reservations.html')

def donner(request):
    chambre= Chambre.objects.all()
    return render(request ,'chambre\donner.html' ,{'chambres':chambre})


def inscription(request):
    return render(request ,'chambre\inscription.html')    
    

def create(request):
    form = ClientForm()
    if request.method == 'POST':
        #print(request.POST)
        form =ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form}
    return render(request ,'chambre\inscription.html' , context)



def update(request,pk):
    Plannings = Planning.objects.get(id=pk)
    form = PlanningForm(instance=Plannings)
    if request.method == 'POST':
        #print(request.POST)
        form =PlanningForm(request.POST,instance=Plannings )
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request ,'chambre\mim.html' , context)



def delete(request,pk):
    Plannings = Planning.objects.get(id=pk)
    if request.method == 'POST':
        Plannings.delete()
        return redirect('/')
    
    context ={'Plannings':Plannings}
    return render(request ,'chambre\mam.html' , context)



def create1(request):
    form= ReservationForm()
    if request.method == 'POST':
        #print(request.POST)
        form =ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form}
    return render(request ,'chambre\Reservations.html' , context)
