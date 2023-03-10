# Generated by Django 4.1.5 on 2023-02-05 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0006_alter_clothes_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='clothes',
            name='garment_image',
            field=models.ImageField(blank=True, null=True, upload_to='products_img'),
        ),
        migrations.AddField(
            model_name='clothes',
            name='size',
            field=models.CharField(default='null', max_length=123, verbose_name='Talles'),
            preserve_default=False,
        ),
    ]
