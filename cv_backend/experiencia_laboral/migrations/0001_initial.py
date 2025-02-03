# Generated by Django 5.0.4 on 2024-06-10 17:40

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_user', '0003_userprofile_user'),
        ('core', '0002_tag_color'),
        ('multimedia_manager', '0004_alter_mediafile_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienciaLaboral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(help_text='Nombre de la empresa donde trabajaste.', max_length=255, verbose_name='Empresa')),
                ('posicion', models.CharField(help_text='Cargo o posición que ocupaste.', max_length=255, verbose_name='Posición')),
                ('descripcion', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='Descripción')),
                ('fecha_inicio', models.DateField(help_text='Cuándo comenzaste a trabajar aquí.', verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateField(blank=True, help_text='Cuándo terminaste de trabajar aquí. Dejar en blanco si aún trabajas aquí.', null=True, verbose_name='Fecha de fin')),
                ('ubicacion', models.CharField(help_text='Ciudad o lugar de la empresa.', max_length=255, verbose_name='Ubicación')),
                ('publicado', models.BooleanField(default=True, help_text='¿Quieres mostrar esta experiencia laboral?', verbose_name='Mostrar experiencia')),
                ('logo_empresa', models.ForeignKey(blank=True, help_text='Ingrese la foto del logo de la empresa.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo_empresa', to='multimedia_manager.mediafile', verbose_name='Logo de Empresa')),
                ('logo_empresa_fondo', models.ForeignKey(blank=True, help_text='Ingrese el fondo del logo de la empresa.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logo_empresa_fondo', to='multimedia_manager.mediafile', verbose_name='Logo de Empresa fondo')),
                ('tags', models.ManyToManyField(blank=True, related_name='experiencias', to='core.tag', verbose_name='Tags')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiencias_laborales', to='base_user.userprofile', verbose_name='Perfil de usuario')),
            ],
            options={
                'verbose_name': 'Experiencia Laboral',
                'verbose_name_plural': 'Experiencias Laborales',
                'ordering': ['-fecha_inicio'],
            },
        ),
    ]
