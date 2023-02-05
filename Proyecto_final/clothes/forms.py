from django import forms

class ClothesForm(forms.Form):
    CHOICES = (
    ('man', 'Hombre'),
    ('woman', 'Mujer'),
    ('unisex', 'Unisex'),
)
    CATEGORIES = (
        ('Buzos', 'Buzos'),
        ('Remeras', 'Remeras'),
        ('Gorras', 'Gorras'),
    )

    type = forms.CharField(max_length=123, label = 'Tipo de prenda')
    price = forms.FloatField(label = 'Precio')
    stock = forms.BooleanField(required=False, label = 'Disponibilidad (stock)')
    sex = forms.ChoiceField(choices = CHOICES, label = 'Sexo')
    category = forms.ChoiceField(choices = CATEGORIES, label= 'Categoría')
    garment_image = forms.ImageField(label= 'Foto de la prenda')
    size = forms.CharField(max_length=123, label= 'Talles')


class CategoryForm(forms.Form):
    class Meta:
        verbose_name_plural = 'Categories'
    name = forms.CharField(max_length=123, label= 'Nombre')
    description = forms.CharField(max_length=123, label= 'Descripción')