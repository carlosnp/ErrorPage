from django.urls import path, include
from .views import *

app_name = 'users'

urlpatterns = [
	path('', UserView.as_view(), name='home'),
	path('list/', UserListView.as_view(), name='list'),
	path('create/', UserCreateView.as_view(), name='create'),
	path('<int:pk>', UserDetailView.as_view(), name='detail'),
	path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
	path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
]