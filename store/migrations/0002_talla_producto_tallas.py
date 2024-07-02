# Generated by Django 4.1.2 on 2024-06-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talla', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tallas',
            field=models.ManyToManyField(to='store.talla'),
        ),
    ]
