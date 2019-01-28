from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm,BmiCalculationForm
from django.views.generic import FormView,TemplateView
from django.http import JsonResponse
from .models import Bmi
from decimal import Decimal
# Create your views here.

class BmiLogin(LoginView):
	template_name = 'login.html'

class Signup(FormView):
	form_class = RegistrationForm
	template_name = 'signup.html'

	def form_valid(self,form):
		form.save()
		username = form.cleaned_data.get('username')
		raw_password = form.cleaned_data.get('password1')
		user = authenticate(username=username,password = raw_password)
		login(self.request,user)
		return redirect('home')

class Home(TemplateView):
	template_name = 'home.html'

class BmiCalculation(FormView):
	form_class = BmiCalculationForm
	template_name = 'bmi_calculation_form.html' 

	def post(self,request,*args,**kwargs):
		height_in_meter = request.POST.get('height_in_meter')
		weight_in_kg = request.POST.get('weight_in_kg')
		bmi_data = Bmi.calculate_bmi(Decimal(height_in_meter),Decimal(weight_in_kg))
		return JsonResponse({'bmi':bmi_data,'h':Decimal(height_in_meter),'w':Decimal(weight_in_kg)})