# Generated by Django 4.2.1 on 2023-05-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetapp', '0004_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]