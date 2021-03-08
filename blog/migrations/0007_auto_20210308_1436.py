# Generated by Django 2.2.19 on 2021-03-08 17:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210308_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, default=1, upload_to='images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])]),
            preserve_default=False,
        ),
    ]
