# Generated by Django 2.2.19 on 2021-03-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210308_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.FileField(blank=True, upload_to='images'),
        ),
    ]