from django.contrib import admin
from.models import Stduent
# Register your models here.
@admin.register(Stduent)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
    
