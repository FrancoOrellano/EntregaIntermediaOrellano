from django import forms

class ClothesForm(forms.Form):
    type = forms.CharField(max_length=123)
    price = forms.FloatField()
    stock = forms.BooleanField(required=False)