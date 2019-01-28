from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
class State(models.Model):
	name = models.CharField(max_length=255,unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	publish = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

class District(models.Model):
	name = models.CharField(max_length=255,unique=True)
	state = models.ForeignKey(State,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	publish = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

class Profession(models.Model):
	name = models.CharField(max_length=255,unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	publish = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

class AcademicLevel(models.Model):
	name = models.CharField(max_length=255,unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	publish = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

class Person(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=255)
	middle_name = models.CharField(max_length=255,null=True,blank=True)
	last_name = models.CharField(max_length=255)
	contact = models.CharField(max_length=255)
	state = models.ForeignKey(State,on_delete=models.CASCADE)
	district = models.ForeignKey(District,on_delete=models.CASCADE)
	address = models.CharField(max_length=255)
	profession = models.ForeignKey(Profession,on_delete=models.CASCADE)
	academic_level = models.ForeignKey(AcademicLevel,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=False)

	def __str__(self):
		return self.contact

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)

class Bmi(models.Model):
	person = models.ForeignKey(Person,on_delete=models.CASCADE)
	height_meter = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(1)])
	weight_kilogram = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(1)])
	bmi = models.DecimalField(max_digits=10,decimal_places=2,blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.person.first_name 

	def save(self,*args,**kwargs):
		self.bmi = self.weight_kilogram / (self.height_meter**2)
		super().save(*args,**kwargs)

	@staticmethod
	def calculate_bmi(height_in_meter,weight_in_kilogram):
		return weight_in_kilogram / (height_in_meter**2)