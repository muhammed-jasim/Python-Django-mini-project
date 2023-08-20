from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Details)
admin.site.register(Teachers)
class contactAdmin(admin.ModelAdmin):
    list_display = ('id','user_name','email_id','phone','name')
admin.site.register(Contacts,contactAdmin)
