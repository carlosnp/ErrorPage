# Django
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
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

class UserCreateView(CreateView):
	template_name = 'users/create.html'
	form_class = UserModelForm
	queryset = UserModel.objects.all()
	success_url = reverse_lazy("users:list")

class UserUpdateView(UpdateView):
	template_name = 'users/create.html'
	form_class = UserModelForm
	queryset = UserModel.objects.all()
	
	def get_success_url(self):
		return reverse("users:detail", kwargs={'pk': self.object.pk})

class UserDeleteView(DeleteView):
	template_name = 'users/delete.html'
	queryset = UserModel.objects.all()
	success_url = reverse_lazy("users:list")