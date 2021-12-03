from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = '__all__'
        widgets = {
            'start': forms.DateInput(format=('%d/%m/%Y'), attrs={'type':'date'}),
            'end': forms.DateInput(format=('%d/%m/%Y'), attrs={'type':'date'})
        }