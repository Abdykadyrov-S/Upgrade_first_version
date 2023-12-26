# Generated by Django 4.2.7 on 2023-12-23 17:57

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_alter_settings_logo_dark_alter_settings_logo_light'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('job', models.CharField(max_length=255, verbose_name='Должность')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='team_img/', verbose_name='Фотография')),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True, verbose_name='whatsapp')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram преподователя')),
            ],
            options={
                'verbose_name': 'Наша команда',
                'verbose_name_plural': 'Наша команда',
            },
        ),
    ]
