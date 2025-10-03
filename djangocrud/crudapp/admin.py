from django.contrib import admin

from .models import student

@admin.register(student)
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display = ['id','name','email']