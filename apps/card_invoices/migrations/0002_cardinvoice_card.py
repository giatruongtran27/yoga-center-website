# Generated by Django 3.0.2 on 2020-04-20 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('card_invoices', '0001_initial'),
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardinvoice',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_invoices', to='cards.Card', verbose_name='card'),
        ),
    ]