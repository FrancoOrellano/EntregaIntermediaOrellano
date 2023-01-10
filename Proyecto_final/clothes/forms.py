from django import forms

class ClothesForm(forms.Form):
    type = forms.CharField(max_length=123, label = 'Tipo de prenda')
    price = forms.FloatField(label = 'Precio')
    stock = forms.BooleanField(required=False, label = 'Disponibilidad (stock)')