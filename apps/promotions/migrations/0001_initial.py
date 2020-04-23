# Generated by Django 3.0.2 on 2020-04-20 03:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, verbose_name='name')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('description', models.CharField(max_length=255, verbose_name='description')),
                ('image', models.ImageField(null=True, upload_to='promotions/', verbose_name='image')),
                ('start_at', models.DateTimeField(blank=True, null=True, verbose_name='start at')),
                ('end_at', models.DateTimeField(blank=True, null=True, verbose_name='end at')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PromotionCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PromotionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.IntegerField(choices=[(0, 'Cash promotion'), (1, 'Plus lesson practice promotion'), (2, 'Plus week practice promotion'), (3, 'Plus month practice promotion'), (4, 'Gift promotion'), (5, 'Percent promotion')], verbose_name='category')),
                ('value', models.FloatField(verbose_name='value or quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='promotion_types', to='shop.Product', verbose_name='product')),
                ('promotion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion_types', to='promotions.Promotion', verbose_name='promotion')),
            ],
        ),
        migrations.CreateModel(
            name='PromotionCodeProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion_code_products', to='shop.Product')),
                ('promotion_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promotion_code_products', to='promotions.PromotionCode')),
            ],
        ),
        migrations.AddField(
            model_name='promotioncode',
            name='products',
            field=models.ManyToManyField(through='promotions.PromotionCodeProduct', to='shop.Product'),
        ),
        migrations.AddField(
            model_name='promotioncode',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='promotions.Promotion', verbose_name='promotion'),
        ),
        migrations.AddField(
            model_name='promotioncode',
            name='promotion_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='codes', to='promotions.PromotionType', verbose_name='promotion type'),
        ),
        migrations.CreateModel(
            name='ApplyPromotionCode',
            fields=[
                ('promotion_code', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='apply', serialize=False, to='promotions.PromotionCode')),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'unique_together': {('content_type', 'object_id')},
            },
        ),
    ]