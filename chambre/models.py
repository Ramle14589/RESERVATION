from django.db import models

# Create your models here.


class Tag(models.Model):
    nom=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.nom




class Client(models.Model):
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    age=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.email




    
    


class Chambre(models.Model):
    ETAGE=(
        ('etage1','etage1'),
        ('etage2','etage2'),
        ('etage3','etage3'),
        ('etage4','etage5')
    )
    
    etage=models.CharField(max_length=100,null=True,choices=ETAGE)
    nom_ch=models.CharField(max_length=100,null=True)
    dispo=models.CharField(max_length=100,null=True)  
    paice=models.FloatField(max_length=100,null=True)
    image_url=models.ImageField(null=True) 


    def __str__(self):
        return self.nom_ch[:50] 


class Reservation(models.Model):

    date_dedutR=models.DateTimeField(null=True)
    date_finR=models.DateTimeField(null=True)
    client=models.ForeignKey(Client, null=True ,on_delete=models.SET_NULL)
    Chambre=models.ForeignKey(Chambre, null=True ,on_delete=models.SET_NULL)
    Tag=models.ManyToManyField(Tag)
   

    

class Planning(models.Model):
    
    date_d=models.DateTimeField(null=True)
    date_f=models.DateTimeField(null=True)
    Client=models.ForeignKey(Client, null=True ,on_delete=models.SET_NULL)
    Chambre=models.ForeignKey(Chambre, null=True ,on_delete=models.SET_NULL)
    Reservation=models.ForeignKey(Reservation, null=True ,on_delete=models.SET_NULL)


    


   