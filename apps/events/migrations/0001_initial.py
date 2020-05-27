# Generated by Django 3.0.2 on 2020-05-27 06:36

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='slug')),
                ('image', models.ImageField(null=True, upload_to='events/', verbose_name='image')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content')),
                ('max_people', models.IntegerField(blank=True, null=True, verbose_name='max people')),
                ('location', models.CharField(max_length=255, verbose_name='location')),
                ('start_at', models.DateField(verbose_name='start at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
        ),
    ]
