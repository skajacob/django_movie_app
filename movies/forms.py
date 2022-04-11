"""Forms from movies app"""

from datetime import date

from django import forms

from .models import Director


class DirectorForm(forms.Form):
    """Director form"""
    first_name = forms.CharField()
    last_name = forms.CharField()
    birthday = forms.DateField(required=False)

    def clean_birthday(self):
        birthday = self.cleaned_data.get("birthday")

        if birthday > date.today():
            raise forms.ValidationError("El cumpleaños está en el futuro")

        return birthday

    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        director_exists = Director.objects.filter(
            first_name=first_name,
            last_name=last_name
        ).exists()

        if director_exists:
            raise forms.ValidationError("El director ya existe")

        return self.cleaned_data

    def save(self):
        director = Director(**self.cleaned_data)
        return director.save()


class DirectorModelForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

    def clean_birthday(self):
        birthday = self.cleaned_data.get("birthday")

        if birthday > date.today():
            raise forms.ValidationError("El cumpleaños está en el futuro")

        return birthday

    def clean(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")

        director_exists = Director.objects.filter(
            first_name=first_name,
            last_name=last_name
        ).exists()

        if director_exists:
            raise forms.ValidationError("El director ya existe")

        return self.cleaned_data