# Generated by Django 4.1.3 on 2022-12-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Content', '0003_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
