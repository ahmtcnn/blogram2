from django import forms
from .models import CustomUser

class LoginForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password',
        ]

class AccountForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'birth_date',
            'blogname',
            'description',
            'photo',
        ]
