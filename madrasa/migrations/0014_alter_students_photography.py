# Generated by Django 4.0.2 on 2022-03-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa', '0013_alter_registration_photography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='photography',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]