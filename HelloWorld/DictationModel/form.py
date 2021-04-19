from django import forms
from django.core.validators import ValidationError
from .models import Category
from HelloWorld.Common import common


class UploadSoundForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all())
    level = forms.ChoiceField(choices=common.LEVEL_LIST, initial=3)
    sound = forms.FileField(
        label='Sound')


class ChoiceWordForm(forms.Form):
    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    level = forms.MultipleChoiceField(
        choices=common.LEVEL_LIST, required=False, widget=forms.CheckboxSelectMultiple,
        initial=[x[0] for x in common.LEVEL_LIST]
    )
