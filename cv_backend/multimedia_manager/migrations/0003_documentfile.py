# Generated by Django 5.0.4 on 2024-04-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia_manager', '0002_mediafile_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título del Documento')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Carga')),
                ('file', models.FileField(help_text='Suba un archivo PDF.', upload_to='documents/', verbose_name='Archivo')),
            ],
            options={
                'verbose_name': 'Archivo de Documento',
                'verbose_name_plural': 'Archivos de Documentos',
            },
        ),
    ]
