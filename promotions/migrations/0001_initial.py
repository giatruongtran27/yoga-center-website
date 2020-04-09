# Generated by Django 3.0.2 on 2020-04-09 01:37

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='name')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description')),
                ('image', models.ImageField(null=True, upload_to='promotions/', verbose_name='image')),
                ('start_at', models.DateTimeField(blank=True, null=True, verbose_name='start at')),
                ('end_at', models.DateTimeField(blank=True, null=True, verbose_name='end at')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PromotionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(0, 'Cash promotion'), (1, 'Plus time practice promotion'), (2, 'Gift promotion'), (3, 'Percent promotion')], verbose_name='category')),
                ('amount', models.FloatField(verbose_name='amount')),
                ('unit', models.IntegerField(choices=[(0, 'Money Unit'), (1, 'Lesson Unit'), (2, 'Week practice unit'), (3, 'Month practice unit'), (4, 'Product unit'), (5, 'Percent unit')], verbose_name='unit')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion_types', to='promotions.Promotion', verbose_name='promotion')),
            ],
        ),
    ]
