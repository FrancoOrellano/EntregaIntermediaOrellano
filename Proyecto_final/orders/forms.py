from django import forms

class OrderForm(forms.Form):
    CHOICES = (
    ('Cash', 'Cash'),
    ('Card', 'Card'),
)
    client = forms.CharField(max_length=123)
    garment = forms.CharField(max_length=123)
    creation_time = forms.DateTimeField()
    payment_method = forms.CharField(max_length=4)