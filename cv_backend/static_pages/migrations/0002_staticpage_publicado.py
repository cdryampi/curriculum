# Generated by Django 5.0.4 on 2024-05-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticpage',
            name='publicado',
            field=models.BooleanField(default=False, help_text='Indica si tu página estatica esta publicada.', verbose_name='Publicado'),
        ),
    ]
