from django import forms

class OrderForm(forms.Form):
    CHOICES = (
    ('Cash', 'Efectivo'),
    ('Card', 'Tarjeta'),
)
    client = forms.CharField(max_length=123, label = 'Cliente')
    garment = forms.CharField(max_length=123, label = 'Prenda')
    payment_method = forms.ChoiceField(choices = CHOICES, label = 'Metodo de pago')