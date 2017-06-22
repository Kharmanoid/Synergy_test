import re

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def name_validator(value):
    if not value.replace(' ', '').isalpha():
        raise ValidationError('Name cannot contain digits!')


def phone_validator(value):
    if not re.match(r'\+380\d{9}', value):
        raise ValidationError(
            _('%(value)s should be in format: +380*********'),
            params={'value': value},
        )


class UserForm(forms.Form):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    name = forms.CharField(max_length=50,
                           label="Name",
                           validators=[name_validator],
                           widget=forms.TextInput(attrs={"class": "form-control form-radius"}))

    mail = forms.EmailField(label="E-mail",
                            widget=forms.EmailInput(attrs={"class": "form-control form-radius"}))

    phone = forms.CharField(max_length=15,
                            required=False,
                            label="Phone",
                            validators=[phone_validator],
                            widget=forms.TextInput(attrs={"class": "form-control form-radius"}))

    mobile = forms.CharField(max_length=15,
                             required=False,
                             label="Mobile Phone",
                             validators=[phone_validator],
                             widget=forms.TextInput(attrs={"class": "form-control form-radius"}))

    status = forms.ChoiceField(choices=[(1, "Inactive"), (2, "Active")],
                               required=False,
                               label="Status",
                               widget=forms.Select(attrs={"class": "form-control form-radius"}))
