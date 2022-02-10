from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.main,name="home"),
    path('Reservations/',views.Reservations ,name="Reservations"),
    path('Plannings/',views.Plannings ,name="Plannings"),
    path('donner/',views.donner, name="donner"),
    path('inscription/',views.inscription, name="inscription"),
    path('create/',views.create , name="create"),
    path('create1/',views.create1 , name="create1"),
    path('update/<str:pk>',views.update , name="update"),
    path('delete/<str:pk>',views.delete , name="delete"),
    path('Clients/<str:pk>',views.Clients,name="Clients")
    
]
 