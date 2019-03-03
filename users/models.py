# Django
from django.db import models
from django.urls import reverse, reverse_lazy

class UserModel(models.Model):
	first_name 	= models.CharField(max_length = 50, null = True, blank = True, verbose_name='Nombre')
	last_name 	= models.CharField(max_length = 80, null = True, blank = True, verbose_name='Apellido')
	username 	= models.CharField(max_length = 80, null = True, blank = True, verbose_name='Nombre de Usuario', unique=True)
	phone 		= models.CharField(max_length=14, unique=True, verbose_name="Teléfono")
	email 		= models.EmailField(verbose_name='Email')
	timestamp 	= models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Fecha de Creación')
	updated 	= models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Fecha de Actualización')

	def __str__(self):
		return str(self.username)
	
	def get_absolute_url(self):
		return reverse("users:detail", kwargs={"pk": self.pk})
	
	class Meta:
		verbose_name='USUARIO'
		verbose_name_plural='USUARIOS'