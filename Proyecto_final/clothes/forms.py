from django import forms

class ClothesForm(forms.Form):
    CHOICES = (
    ('man', 'Hombre'),
    ('woman', 'Mujer'),
    ('unisex', 'Unisex'),
)
    CATEGORIES = (
        ('jumpers', 'Buzos'),
        ('shirts', 'Remeras'),
        ('caps', 'Gorras'),
    )

    type = forms.CharField(max_length=123, label = 'Tipo de prenda')
    price = forms.FloatField(label = 'Precio')
    stock = forms.BooleanField(required=False, label = 'Disponibilidad (stock)')
    sex = forms.ChoiceField(choices = CHOICES, label = 'Sexo')
    category = forms.ChoiceField(choices = CATEGORIES, label= 'Categoría')


class CategoryForm(forms.Form):
    class Meta:
        verbose_name_plural = 'Categories'
    name = forms.CharField(max_length=123, label= 'Nombre')
    description = forms.CharField(max_length=123, label= 'Descripción')