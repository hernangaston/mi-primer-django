# Generated by Django 2.0.1 on 2018-01-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('biblioteca', '0003_auto_20180115_1642'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Libros',
            new_name='Libro',
        ),
        migrations.AlterField(
            model_name='autor',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
    ]
