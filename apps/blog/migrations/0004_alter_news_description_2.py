# Generated by Django 4.2.7 on 2023-12-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_news_description_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description_2',
            field=models.TextField(verbose_name='короткое описание новости'),
        ),
    ]
