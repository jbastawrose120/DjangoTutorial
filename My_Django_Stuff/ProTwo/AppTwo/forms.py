from django import forms
from AppTwo.models import User

class NewUserForm(forms.ModelForm):
    #custom validations would need to go here
    class Meta:
        model = User
        fields = '__all__'
