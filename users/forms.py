# Django
from django import forms
# Porject
from .models import UserModel

class UserModelForm(forms.ModelForm):
    username    = forms.CharField(min_length=4,max_length = 50, required=True, label="Nombre de Usuario")
    first_name  = forms.CharField(min_length=4,max_length = 80, label="Nombre")
    last_name   = forms.CharField(min_length=4,max_length = 80, label="Apellido")
    class Meta:
        model = UserModel
        fields =[
        	'username',
            'first_name',
            'last_name',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = self.fields['username'].label
        self.fields['first_name'].widget.attrs['placeholder'] = self.fields['first_name'].label
        self.fields['last_name'].widget.attrs['placeholder'] = self.fields['last_name'].label
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label
        for key in self.fields:
            self.fields[key].widget.attrs.update({'class':'userform'})