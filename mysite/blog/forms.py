#from django import forms
#from blog.models import Persona

#class Registro(forms.ModelForm):

    #class Meta:
       # model = Persona

        #fields = [

            #'nombre',
            #'rut',
            #'email',
            #'fecha_nac',
            #'telefono',
            #'region',
            #'comuna',
            #'casa',
        #]

        #labels = {
            #'nombre' : 'nombre',
            #'rut' : 'rut',
            #'email' : 'email',
			#'fecha_nac' : 'calendar',
            #'telefono' : 'telefono',
            #'region' : 'region',
            #'comuna' : 'comuna',
            #'casa' : 'casa',     
        #}

        #widgets = {

            #'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            #'rut' : forms.TextInput(attrs={'class':'form-control'}),
            #'email' : forms.EmailInput(attrs={'class':'form-control'}),
            #'fecha_nac' : forms.DateInput(attrs={'class':'form-control'}),
            #'telefono' : forms.TextInput(attrs={'class':'form-control'}),
            #'region' : forms.Select(attrs={'class':'form-control'}),
            #'comuna' : forms.Select(attrs={'class':'form-control'}),
            #'casa' : forms.Select(attrs={'class':'form-control'}),
        #}    


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class RegistroForm(UserCreationForm):


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

    labels = {
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
    }





