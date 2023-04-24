from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', "surname", 'birth_date')
        #birth_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
        widgets = {
            'birth_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }


