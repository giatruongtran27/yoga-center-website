# Generated by Django 3.0.2 on 2020-03-25 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('lectures', '0001_initial'),
        ('rooms', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.IntegerField(choices=[(0, 'Active'), (2, 'Inactive')], default=0, verbose_name='state')),
                ('date', models.DateField(verbose_name='date')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='start time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='end time')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='notes')),
                ('is_full', models.BooleanField(default=False, verbose_name='is full')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('lectures', models.ManyToManyField(related_name='lessons', to='lectures.Lecture', verbose_name='lectures')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='rooms.Room', verbose_name='room')),
                ('substitute_trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='substitute_lessons', to='classes.YogaClass', verbose_name='substitute trainer')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='core.Trainer', verbose_name='trainer')),
                ('yogaclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='classes.YogaClass', verbose_name='yogaclass')),
            ],
        ),
    ]
