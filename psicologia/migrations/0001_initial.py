# Generated by Django 2.0.1 on 2018-03-06 20:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_autorizacion', models.DateField()),
                ('presentada', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Autorizaciones',
                'ordering': ['fecha_autorizacion'],
            },
        ),
        migrations.CreateModel(
            name='ObraSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
            ],
            options={
                'verbose_name_plural': 'Obras Sociales',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('dni', models.IntegerField()),
                ('historia', models.TextField()),
                ('medicacion', models.CharField(max_length=70)),
                ('diagnostico', models.TextField()),
                ('inicio_tratamiento', models.DateTimeField(default=django.utils.timezone.now)),
                ('obra_social', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='psicologia.ObraSocial')),
            ],
            options={
                'verbose_name_plural': 'Pacientes',
                'ordering': ['apellido'],
            },
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profesionales',
                'ordering': ['matricula'],
            },
        ),
        migrations.CreateModel(
            name='SesionTerapeutica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datos', models.TextField()),
                ('fecha_sesion', models.DateField()),
                ('facturada', models.BooleanField()),
                ('numero_sesion', models.IntegerField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psicologia.Paciente')),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psicologia.Profesional')),
            ],
            options={
                'verbose_name_plural': 'Sesiones Terapeuticas',
                'ordering': ['fecha_sesion'],
            },
        ),
        migrations.AddField(
            model_name='paciente',
            name='profesional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psicologia.Profesional'),
        ),
        migrations.AddField(
            model_name='autorizacion',
            name='obra_social',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='psicologia.ObraSocial'),
        ),
        migrations.AddField(
            model_name='autorizacion',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='psicologia.Paciente'),
        ),
        migrations.AddField(
            model_name='autorizacion',
            name='profesional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psicologia.Profesional'),
        ),
    ]
