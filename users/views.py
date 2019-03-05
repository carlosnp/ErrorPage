# Django
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# Project
from .models import *
from .forms import *

class UserView(TemplateView):
    template_name = "users/home.html"

class UserListView(ListView):
	template_name = 'users/list.html'
	queryset = UserModel.objects.all()

class UserDetailView(DetailView):
	template_name = 'users/detail.html'
	queryset = UserModel.objects.all()

class UserCreateView(SuccessMessageMixin, CreateView):
	template_name = 'users/create.html'
	form_class = UserModelForm
	queryset = UserModel.objects.all()
	success_message = 'Se creo el usuario %(username)s satisfactoriamente'
	success_url = reverse_lazy("users:list")

	def get_success_message(self, cleaned_data):
		return self.success_message % dict(cleaned_data, username=self.object.username.upper(),)

class UserUpdateView(SuccessMessageMixin, UpdateView):
	template_name = 'users/create.html'
	form_class = UserModelForm
	queryset = UserModel.objects.all()
	success_message = 'Se actualizo el usuario %(username)s satisfactoriamente'

	def get_success_message(self, cleaned_data):
		return self.success_message % dict(cleaned_data, username=self.object.username.upper(),)
	
	def get_success_url(self):
		return reverse("users:detail", kwargs={'pk': self.object.pk})

class UserDeleteView(DeleteView):
	template_name = 'users/delete.html'
	queryset = UserModel.objects.all()
	success_url = reverse_lazy("users:list")
	success_message = 'Se Elimino el usuario satisfactoriamente'

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super(UserDeleteView, self).delete(request, *args, **kwargs)

class UserDelete(View):

    def post(self, request, *args, **kwargs):
        users = request.POST.get('users', None)
        users = UserModel.objects.get(pk=int(users))
        users.delete()
        messages.add_message(request, messages.SUCCESS,'El usuario se ha Eliminado satisfactoriamente.')
        return redirect("UserListView")