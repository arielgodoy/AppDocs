# Generated by Django 4.2.3 on 2023-07-25 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=20)),
                ('rol', models.CharField(choices=[('persona', 'Persona Natural'), ('sociedad', 'Sociedad')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.propietario')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(upload_to='archivos_documentos/')),
                ('propiedad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.propiedad')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.tipodocumento')),
            ],
        ),
    ]
