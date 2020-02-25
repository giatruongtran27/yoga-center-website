# Generated by Django 3.0.2 on 2020-02-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='name')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='course', verbose_name='image')),
                ('course_type', models.IntegerField(choices=[(0, 'Practice Course'), (1, 'Training Course')], default=0, verbose_name='course type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='end at')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
                'ordering': ('created_at', 'name'),
            },
        ),
    ]
