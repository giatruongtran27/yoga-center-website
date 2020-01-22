# Generated by Django 3.0.2 on 2020-01-22 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YogaClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='class')),
                ('state', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive')], default=0)),
                ('level', models.IntegerField(choices=[(0, 'Basic Level'), (1, 'Intermediate Level'), (2, 'Advanced Level')], default=0)),
                ('price_per_lesson', models.FloatField(blank=True, null=True)),
                ('price_per_month', models.FloatField(blank=True, null=True)),
                ('price_course', models.FloatField(blank=True, null=True)),
                ('max_people', models.IntegerField(blank=True, null=True)),
                ('start_at', models.DateTimeField(blank=True, null=True)),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='courses.Course')),
            ],
            options={
                'verbose_name': 'Yoga Class',
                'verbose_name_plural': 'Yoga Classes',
                'ordering': ('created_at', 'name'),
            },
        ),
    ]
