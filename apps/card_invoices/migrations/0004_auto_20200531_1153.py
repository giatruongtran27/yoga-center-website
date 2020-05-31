# Generated by Django 3.0.2 on 2020-05-31 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20200527_1336'),
        ('card_invoices', '0003_cardinvoice_payment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardinvoice',
            name='id',
        ),
        migrations.AlterField(
            model_name='cardinvoice',
            name='card',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='invoice', serialize=False, to='cards.Card', verbose_name='card'),
        ),
    ]