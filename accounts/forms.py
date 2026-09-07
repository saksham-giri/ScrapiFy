from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistrationUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone",
            "role",
            "password1",
            "password2",
        ]
        


class LoginUser(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        widget=forms.PasswordInput
    )


