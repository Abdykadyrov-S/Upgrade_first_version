# Generated by Django 4.2.7 on 2023-12-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Настройки сайта', 'verbose_name_plural': 'Настройки сайта'},
        ),
        migrations.AddField(
            model_name='data',
            name='clients_title',
            field=models.CharField(default=1, max_length=155, verbose_name='Заголовок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='employees_title',
            field=models.CharField(default=1, max_length=155, verbose_name='Введите значение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='orders_title',
            field=models.CharField(default=1, max_length=155, verbose_name='Заголовок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='products_title',
            field=models.CharField(default=1, max_length=155, verbose_name='Заголовок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='data',
            name='clients',
            field=models.CharField(default='0', max_length=155, verbose_name='Введите значение'),
        ),
        migrations.AlterField(
            model_name='data',
            name='employees',
            field=models.CharField(default='0', max_length=155, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='data',
            name='orders',
            field=models.CharField(default='0', max_length=155, verbose_name='Введите значение'),
        ),
        migrations.AlterField(
            model_name='data',
            name='products',
            field=models.CharField(default='0', max_length=155, verbose_name='Введите значение'),
        ),
    ]
