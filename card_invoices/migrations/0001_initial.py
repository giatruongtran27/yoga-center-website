# Generated by Django 3.0.2 on 2020-03-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='amount')),
                ('charge_id', models.CharField(blank=True, max_length=256, null=True, verbose_name='charge id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
        ),
    ]
