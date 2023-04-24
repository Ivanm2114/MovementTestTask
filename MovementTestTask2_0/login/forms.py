from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'my_date': forms.DateInput(attrs={'type':'date'})
        }