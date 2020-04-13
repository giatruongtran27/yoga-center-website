# Generated by Django 3.0.2 on 2020-04-13 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promotions', '0002_auto_20200413_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotiontype',
            name='unit',
        ),
        migrations.AlterField(
            model_name='promotiontype',
            name='category',
            field=models.IntegerField(choices=[(0, 'Cash promotion'), (1, 'Plus lesson practice promotion'), (2, 'Plus week practice promotion'), (3, 'Plus month practice promotion'), (4, 'Gift promotion'), (5, 'Percent promotion')], verbose_name='category'),
        ),
    ]