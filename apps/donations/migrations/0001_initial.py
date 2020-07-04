# Generated by Django 3.0.2 on 2020-07-04 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True, verbose_name='phone number')),
                ('content', models.CharField(max_length=255, verbose_name='content')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='amount')),
                ('charge_id', models.CharField(blank=True, max_length=256, null=True, verbose_name='charge id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
        ),
    ]
