# Generated by Django 4.2 on 2023-04-29 06:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='products/', verbose_name='Şəkil'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new',
            name='photo',
            field=models.ImageField(upload_to='news/', verbose_name='Şəkil'),
        ),
    ]