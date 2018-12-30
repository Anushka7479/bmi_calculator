from django.contrib import admin
from .models import State,District,Profession,AcademicLevel,Person,Bmi
# Register your models here.
admin.site.register([State,District,Profession,AcademicLevel,Person,Bmi])