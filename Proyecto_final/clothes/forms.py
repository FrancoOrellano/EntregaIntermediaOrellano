from django import forms

class ClothesForm(forms.Form):
    CHOICES = (
    ('man', 'Hombre'),
    ('woman', 'Mujer'),
    ('unisex', 'Unisex'),
)
    type = forms.CharField(max_length=123, label = 'Tipo de prenda')
    price = forms.FloatField(label = 'Precio')
    stock = forms.BooleanField(required=False, label = 'Disponibilidad (stock)')
    sex = forms.ChoiceField(choices = CHOICES, label = 'Sexo')


class CategoryForm(forms.Form):
    class Meta:
        verbose_name_plural = 'Categories'
    name = forms.CharField(max_length=123, label= 'Nombre')
    description = forms.CharField(max_length=123, label= 'Descripción')