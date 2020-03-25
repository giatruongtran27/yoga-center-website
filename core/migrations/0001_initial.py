# Generated by Django 3.0.2 on 2020-03-25 09:03

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_trainee', models.BooleanField(default=False, verbose_name='is trainee')),
                ('is_trainer', models.BooleanField(default=False, verbose_name='is trainer')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='slug')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be valid', regex='^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\\s\\./0-9]*$')], verbose_name='phone number')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='birth day')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='address')),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (0, 'Male')], default=1, verbose_name='gender')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='country')),
                ('language', models.CharField(blank=True, max_length=255, null=True, verbose_name='language')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile', verbose_name='image')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated_at')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='staff', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('work_experience', models.TextField(blank=True, verbose_name='work experience')),
                ('is_student', models.BooleanField(default=False, verbose_name='is student')),
                ('graduate_school', models.CharField(blank=True, max_length=255, null=True, verbose_name='graduate school')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='company name')),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='trainee', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('health_condition', models.TextField(blank=True, verbose_name='health condition')),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='trainer', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('yoga_teaching_experience', models.TextField(blank=True, verbose_name='yoga teaching experience')),
                ('is_student', models.BooleanField(default=False, verbose_name='is student')),
                ('graduate_school', models.CharField(blank=True, max_length=255, null=True, verbose_name='graduate school')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='company name')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='description')),
                ('image', models.ImageField(blank=True, upload_to='certificates', verbose_name='image')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
    ]
