# Generated by Django 4.1.7 on 2023-05-02 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='unvanlink',
            field=models.CharField(default=datetime.datetime(2023, 5, 2, 17, 41, 24, 802735, tzinfo=datetime.timezone.utc), max_length=4096, verbose_name='Unvan Linki'),
            preserve_default=False,
        ),
    ]
