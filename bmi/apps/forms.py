from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import State,District,Profession,AcademicLevel

class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(max_length=100)
	middle_name = forms.CharField(max_length=100,required=False)
	last_name = forms.CharField(max_length=100)
	date_of_birth = forms.DateField()
	contact = forms.CharField(max_length=50)
	email = forms.EmailField()
	state = forms.ModelChoiceField(State.objects.filter(publish=True))
	district = forms.ModelChoiceField(District.objects.filter(publish=True))
	address = forms.CharField(max_length=100)
	profession = forms.ModelChoiceField(Profession.objects.filter(publish=True))
	academic_level = forms.ModelChoiceField(AcademicLevel.objects.filter(publish=True)) 

	def __init__(self,*args,**kwargs):
		super(RegistrationForm,self).__init__(*args,**kwargs)
		for visible in self.visible_fields(): 
			visible.field.widget.attrs['class'] = 'form-control'

class BmiCalculationForm(forms.Form):
	HEIGHT_CHOICES = (('ft','feet'),('inch','inch'),('mt','meter'),('cm','centimeter'))
	WEIGHT_CHOICES = (('kg','kilogram'),('gm','gram'))
	height_in_meter = forms.DecimalField(max_value=5,min_value=0.01,decimal_places=2,label='Height (meter)')
	height_unit = forms.ChoiceField(choices=HEIGHT_CHOICES)
	weight_in_kg = forms.DecimalField(max_value=500,min_value=1,decimal_places=2,label='Weight (kg)')
	weight_unit = forms.ChoiceField(choices=WEIGHT_CHOICES)

	def __init__(self,*args,**kwargs):
		super(BmiCalculationForm,self).__init__(*args,**kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'

