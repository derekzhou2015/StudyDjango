from django import forms
from django.db.models import Q
from django.core.exceptions import ValidationError
from . import models
from HelloWorld.Common import common


class AccountForm(forms.Form):

    id = forms.CharField(widget=forms.HiddenInput, required=False)
    first_name = forms.CharField(min_length=2, label='First Name', error_messages={
                                 'min_length': 'Your first name is shorter.', 'required': 'Your first name is empty.'}, widget=forms.TextInput(attrs={'placeholder': 'Your first name'}))
    last_name = forms.CharField(min_length=2, label='Last Name', error_messages={
                                'min_length': 'Your last name is shorter.', 'required': 'Your last name is empty.'})
    email = forms.EmailField(label='Email', error_messages={
                             'required': 'Your email is empty.'})
    password = forms.CharField(min_length=3, label='Password', error_messages={
        'min_length': 'Your password is shorter.', 'required': 'Your password is empty.'})
    gender = forms.ChoiceField(
        label='Gender', choices=common.GENDER_LIST, initial='2')
    tel = forms.CharField(min_length=6, label='Telephone', error_messages={
        'min_length': 'Your tellphone is shorter.', 'required': 'Your telephone number is empty.'})
    addr = forms.CharField(label='Address', error_messages={
        'required': 'Your address is empty.'})
    birthday = forms.DateField(label='Birthday', error_messages={
                               'required': 'Your birthday is empty.'})

    def clean_email(self):
        val = self.cleaned_data.get('email')
        if models.Account.objects.filter(email=val):
            raise ValidationError('This email is existed.')
        return val


class AccountEditForm(AccountForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        id = self.cleaned_data.get('id')
        if models.Account.objects.all().filter(~Q(id=id), email=email):
            raise ValidationError('This email is existed.')
        return email
