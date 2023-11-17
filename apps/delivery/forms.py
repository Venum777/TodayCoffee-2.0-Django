from django import forms
from django.forms import ModelForm
from django.db import models

from delivery.models import Delivery
from auths.models import MyUser


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = "__all__"
        exclude = ['user', 'created_tampstamp']

    def save(self, commit=True, *args, **kwargs):
        self.full_clean()
        return super().save(commit=commit, *args, **kwargs)
