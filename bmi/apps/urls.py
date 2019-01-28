from django.urls import path
from .views import BmiLogin,Signup,Home,BmiCalculation

app_name = 'bmi'

urlpatterns = [
	path('',BmiLogin.as_view()),
	path('signup/',Signup.as_view()),
	path('home/',Home.as_view()),
	path('bmi/',BmiCalculation.as_view()),
]