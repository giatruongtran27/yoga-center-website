# Generated by Django 3.0.2 on 2020-03-12 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_yogaclass_trainer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yogaclass',
            old_name='price_course',
            new_name='price_for_training_class',
        ),
    ]
