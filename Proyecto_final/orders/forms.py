from django import forms

class OrderForm(forms.Form):
    CHOICES = (
    ('Cash', 'Cash'),
    ('Card', 'Card'),
)
    client = forms.CharField(max_length=123, label = 'Cliente')
    garment = forms.CharField(max_length=123, label = 'Prenda')
    payment_method = forms.CharField(max_length=4, label = 'Metodo de pago (Card/Cash)')