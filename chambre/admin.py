from django.contrib import admin

# Register your models here.

from .models import *
class ChambreAdmin(admin.ModelAdmin):
    list_display=('nom_ch' ,'paice','dispo')

admin.site.register( Client)
admin.site.register( Chambre,ChambreAdmin)
admin.site.register( Planning)
admin.site.register(Reservation)
admin.site.register(Tag)

