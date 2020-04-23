# Generated by Django 3.0.2 on 2020-04-20 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YogaClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='slug')),
                ('price_per_lesson', models.FloatField(blank=True, null=True, verbose_name='price per lesson')),
                ('price_per_month', models.FloatField(blank=True, null=True, verbose_name='price per month')),
                ('price_for_training_class', models.FloatField(blank=True, null=True, verbose_name='price course')),
                ('max_people', models.IntegerField(blank=True, null=True, verbose_name='max people')),
                ('start_at', models.DateField(blank=True, null=True, verbose_name='start at')),
                ('end_at', models.DateField(blank=True, null=True, verbose_name='end at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='courses.Course', verbose_name='course')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='accounts.Trainer', verbose_name='trainer')),
            ],
        ),
    ]