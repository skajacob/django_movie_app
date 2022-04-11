"""Users forms"""

from django import forms

from users.models import User


class SignupForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password = forms.CharField(required=True)
    password_confirmation = forms.CharField(required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            raise forms.ValidationError("El usuario ya existe")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_exists = User.objects.filter(email=email).exists()
        if email_exists:
            raise forms.ValidationError("El correo ya está en uso")

        return email

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if password != password_confirmation:
            raise forms.ValidationError("Las contraseñas no coinciden")

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')
        return User.objects.create_user(**data)