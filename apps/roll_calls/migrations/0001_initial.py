# Generated by Django 3.0.2 on 2020-04-16 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cards', '0001_initial'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RollCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studied', models.BooleanField(default=False, verbose_name='studied')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roll_calls', to='cards.Card', verbose_name='card')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roll_calls', to='lessons.Lesson', verbose_name='lesson')),
            ],
        ),
    ]
