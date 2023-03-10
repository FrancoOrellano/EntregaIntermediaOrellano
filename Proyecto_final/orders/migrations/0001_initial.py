# Generated by Django 4.1.5 on 2023-01-08 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=123)),
                ('garment', models.CharField(max_length=123)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], max_length=4)),
            ],
        ),
    ]
