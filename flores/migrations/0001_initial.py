# Generated by Django 3.2.4 on 2021-06-07 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flores_en_descuento', models.CharField(max_length=64)),
                ('usuario_con_descuento', models.CharField(max_length=64)),
                ('valor_de_descuento', models.IntegerField()),
            ],
        ),
    ]
