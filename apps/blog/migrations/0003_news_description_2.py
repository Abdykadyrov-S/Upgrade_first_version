# Generated by Django 4.2.7 on 2023-12-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_news_descriptions_news_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description_2',
            field=models.TextField(default=1, verbose_name='Описание новости'),
            preserve_default=False,
        ),
    ]
