import datetime

from django.db import models
from django.template.backends import django
from django.urls import reverse
# Create your models here.

class Agent(models.Model):
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

class Specialist(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    count_service = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Специалисты'
        verbose_name_plural = 'Специалисты'
        ordering = ['-time_create', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('specialist', kwargs={'specialist_slug': self.slug})

class Company(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Агентства'
        verbose_name_plural = 'Агентства'
        ordering = ['-time_create', 'title']

    def get_absolute_url(self):
        return reverse('company', kwargs={'comapny_slug': self.slug})

class Offer(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('offer', kwargs={'offer_slug': self.slug})

class Review(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    content = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse('review', kwargs={'review_slug': self.slug})

class Newbuilding(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    typehome = models.CharField(max_length=255)
    square = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    number = models.CharField(max_length=255)

class Rent(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    square = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    content = models.TextField(blank=True)
    address = models.CharField(max_length=255)
    price = models.IntegerField(default=0)



