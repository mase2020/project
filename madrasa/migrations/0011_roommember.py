# Generated by Django 4.0.2 on 2022-03-21 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrasa', '0010_teachers_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('uid', models.CharField(max_length=1000)),
                ('room_name', models.CharField(max_length=200)),
                ('insession', models.BooleanField(default=True)),
            ],
        ),
    ]
