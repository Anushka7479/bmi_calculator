from django.contrib import admin
from .models import State,District,Profession,AcademicLevel,Person,Bmi
# Register your models here.
admin.site.register(Person)

@admin.register(AcademicLevel)
class AcademicLevelAdmin(admin.ModelAdmin):
	list_display = ('name','created','updated','publish',)
	list_filter = ('name','updated','publish',)
	list_editable = ('publish',)
	search_fields = ('name','updated')

@admin.register(Bmi)
class BmiAdmin(admin.ModelAdmin):
	exclude = ('bmi',)
	list_display = ('height_meter','weight_kilogram','bmi','created')

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
	list_display = ('name','created','updated','publish',)
	list_filter = ('name','updated','publish',)
	list_editable = ('publish',)
	search_fields = ('name','updated')

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
	list_display = ('name','created','updated','publish',)
	list_filter = ('name','updated','publish',)
	list_editable = ('publish',)
	search_fields = ('name','updated')

@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
	list_display = ('name','created','updated','publish',)
	list_filter = ('name','updated','publish',)
	list_editable = ('publish',)
	search_fields = ('name','updated',)

admin.site.site_header = 'BMI'
admin.site.site_title = 'Bmi Calculator'
admin.site.index_title = 'Admin' 