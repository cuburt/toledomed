from django.contrib.auth.models import User
from django import forms
from .models import *
import datetime


class BillingForm(forms.ModelForm):

    date = forms.DateField(widget=forms.TextInput, initial=datetime.datetime.now().date)


    class Meta:
        model = bill
        fields = ['date',
                  'sum_in_words',
                  'sum',
                  'is_full']