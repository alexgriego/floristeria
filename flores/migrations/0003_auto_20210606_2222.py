# Generated by Django 3.2.4 on 2021-06-07 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flores', '0002_compra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('documento', models.CharField(max_length=64)),
                ('direccion', models.FloatField()),
                ('correo', models.CharField(max_length=64)),
                ('tarjeta_de_credito', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='compra',
            name='numero_de_factura',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='compra',
            name='valor_de_compra',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='valor_de_descuento',
            field=models.FloatField(),
        ),
    ]
