# Generated by Django 4.1.2 on 2024-07-17 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0006_alter_boleta_iva_alter_boleta_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoEnvio',
            fields=[
                ('id_metodo', models.AutoField(db_column='id_metodo', primary_key=True, serialize=False)),
                ('desc_metodo', models.CharField(max_length=50)),
                ('precio_metodo', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='boleta',
            name='envio',
            field=models.ForeignKey(db_column='id_metodo', default=None, on_delete=django.db.models.deletion.CASCADE, to='carrito.metodoenvio'),
            preserve_default=False,
        ),
    ]
