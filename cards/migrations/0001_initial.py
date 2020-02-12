# Generated by Django 3.0.2 on 2020-02-11 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('form_of_using', models.IntegerField(choices=[(0, 'Full Month'), (1, 'Consecutive Lessons'), (2, 'Non Consecutive Lessons'), (3, 'Trial'), (4, 'For Training Course')], default=0, verbose_name='form of using')),
                ('min_lessons_require', models.IntegerField(blank=True, null=True, verbose_name='min lessons required')),
                ('multiplier', models.FloatField(null=True, verbose_name='multiplier')),
                ('for_longtime_trainee_only', models.BooleanField(default=False, verbose_name='for longtime trainee only')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.DateField(verbose_name='start_at')),
                ('end_at', models.DateField(verbose_name='end_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at')),
                ('card_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='cards.CardType', verbose_name='card type')),
            ],
        ),
    ]