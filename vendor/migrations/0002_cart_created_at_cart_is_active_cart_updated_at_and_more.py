# Generated by Django 4.2.2 on 2024-01-31 06:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='cart',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor.productcategory'),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='hex_code',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='productcolor',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='established_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_subscribed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]