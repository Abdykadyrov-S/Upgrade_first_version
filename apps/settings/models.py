from django.db import models
from django_resized.forms import ResizedImageField
from ckeditor.fields import RichTextField



# Create your models here.
class Settings(models.Model):
    logo_dark = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип для темной темы",
        blank = True, null = True
    )
    logo_light = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='logo/',
        verbose_name="Логотип для светлой темы",
        blank = True, null = True
    )
    title = models.CharField(
        max_length = 200,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='описание'
    )
    image = models.ImageField(
        upload_to='banner/',
        verbose_name='Баннер'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта',
        blank=True, null=True
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True, null=True
    )
    facebook = models.URLField(
        verbose_name='Facebook',
        blank=True, null=True
    )
    twitter = models.URLField(
        verbose_name='Twitter',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram',
        blank=True, null=True
    )
    telegram = models.URLField(
        max_length=255,
        verbose_name='Telegram',
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"

class About(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    descriptions = RichTextField(
        verbose_name="Информационный текст",
        blank=True,null=True
    )
    image = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "about_image",
        verbose_name="Фотография",
        blank = True,null = True    
    )
    title_2 = models.CharField(
        max_length=255,
        verbose_name="Заголовок №2"
    )
    descriptions_2 = RichTextField(
        verbose_name="Информационный текст №2",
        blank=True,null=True
    )
    image_2 = ResizedImageField(
        force_format = "WEBP",
        quality = "100",
        upload_to = "about_image",
        verbose_name="Фотография №2",
        blank = True,null = True    
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

class Data(models.Model):
    clients_title = models.CharField(
        max_length=155,
        verbose_name="Заголовок",
    )
    clients = models.CharField(
        max_length=155,
        verbose_name="Введите значение",
        default="0"
    )
    employees_title = models.CharField(
        max_length=155,
        verbose_name="Введите значение",
    )
    employees = models.CharField(
        max_length=155,
        verbose_name="Заголовок",
        default="0"
    )
    orders_title = models.CharField(
        max_length=155,
        verbose_name="Заголовок",
    )
    orders = models.CharField(
        max_length=155,
        verbose_name="Введите значение",
        default="0"
    )
    products_title = models.CharField(
        max_length=155,
        verbose_name="Заголовок",
    )
    products = models.CharField(
        max_length=155,
        verbose_name="Введите значение",
        default="0"
    )

    class Meta:
        verbose_name = "Наша статистика"
        verbose_name_plural = "Наша статистика"




class Contact(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name="Имя пользователя",
        null=True,blank=True
    )
    phone = models.CharField(
        max_length=155,
        verbose_name="Номер телефона",
        null=True,blank=True
    )
    cause = models.CharField(
        max_length=155,
        verbose_name="Причина",
        null=True,blank=True
    )
    message = models.TextField(
        verbose_name="Сообщение",
        null=True,blank=True
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Оставленный отзыв"
        verbose_name_plural = "Оставленные отзывы"

class Team(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="ФИО"
    )
    job = models.CharField(
        max_length=255,
        verbose_name="Должность"
    )
    image = ResizedImageField(
        force_format="WEBP",
        quality=100,
        upload_to='team_img/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    whatsapp = models.CharField(
        max_length=255,
        verbose_name='whatsapp',
        blank=True, null=True
    )
    instagram = models.URLField(
        verbose_name='Instagram преподователя',
        blank=True, null=True
    )

    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"