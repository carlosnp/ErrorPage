# Django
from django import forms
# Porject
from .models import UserModel

class UserModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields =[
        	'username',
            'first_name',
            'last_name',
            'email',
        ]