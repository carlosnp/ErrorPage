# Django
from django import forms
# Porject
from .models import UserModel

class UserModelForm(forms.ModelForm):
    username    = forms.CharField(min_length=3,max_length = 50, required=True, label="Nombre de Usuario")
    first_name  = forms.CharField(min_length=3,max_length = 80, label="Nombre")
    last_name   = forms.CharField(min_length=3,max_length = 80, label="Apellido")
    phone       = forms.CharField(min_length=7, max_length=14, label='Teléfono')
    class Meta:
        model = UserModel
        fields =[
        	'username',
            'first_name',
            'last_name',
            'phone',
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['placeholder'] = '04xx-xxx-xxx solo números'
        for key in self.fields:
            self.fields[key].widget.attrs.update({'class':'userform'})
        for key in (field for field in self.fields if field not in ['phone']):
            self.fields[key].widget.attrs['placeholder'] = self.fields[key].label

    def clean(self):
        cleaned_data = super(UserModelForm, self).clean()
        phone = cleaned_data.get("phone")
        username = cleaned_data.get("username")
        # Mensaje de error para el nombre de usuario
        if username.isnumeric():
            msg = ("El Nombre de Usuario debe contener solo letras")
            self.add_error('phone', msg)
        # Mensaje de error para el numero de telefono
        if not phone.isnumeric():
            msg = ("El número de teléfono solo debe contener números")
            self.add_error('phone', msg)