from dataclasses import fields
from  django.forms import  ModelForm 
from .models import *



class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields ="__all__"



class PlanningForm(ModelForm):
    class Meta:
        model = Planning
        fields ="__all__"


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields ="__all__"