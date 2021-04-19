from django import forms
from django.core.validators import ValidationError
from django.db.models import Q
from . import models
from HelloWorld.Common import common
import datetime


class AuthorForm(forms.Form):
    name = forms.CharField(label='Author Name',
                           min_length=2, max_length=32, help_text='*')
    age = forms.DecimalField(label='Age', help_text='*')


class AuthorDetailForm(forms.Form):
    gender = forms.ChoiceField(
        label='Gender', choices=common.GENDER_LIST, initial=2)
    tel = forms.CharField(label='Telephone',
                          min_length=2, max_length=32, help_text='*')
    address = forms.CharField(label='Address', max_length=64)
    birthday = forms.DateField(
        label='Birthday', widget=forms.DateInput({'type': 'date'}))


class PublisherBaseForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput, required=False)
    name = forms.CharField(label='Name', min_length=2, max_length=32, error_messages={'required': 'The publisher\'s name can not be empty. ', 'min_length': 'The publisher\'s name is shorter.'},
                           help_text='*', widget=forms.TextInput({'placeholder': 'publisher name.'}))
    city = forms.CharField(label='City', max_length=64, error_messages={'required': 'city can not be empty. ', 'min_length': 'city is shorter.'},
                           help_text='*', widget=forms.TextInput({'placeholder': 'city.'}))
    email = forms.EmailField(label='Email', error_messages={
        'required': 'email is empty.'}, help_text='*', widget=forms.EmailInput({'placeholder': 'email.'}))


class PublisherAddForm(PublisherBaseForm):
    def clean_name(self):
        val = self.cleaned_data.get('name')
        if models.Publisher.objects.filter(name=val):
            raise ValidationError('This name is existed.')
        return val


class PublisherEditForm(PublisherBaseForm):
    def clean_name(self):
        id = self.cleaned_data.get('id')
        val = self.cleaned_data.get('name')
        obj = models.Publisher.objects.filter(~Q(id=id), name=val).first()
        if obj:
            raise ValidationError('This name is existed.')
        return val
