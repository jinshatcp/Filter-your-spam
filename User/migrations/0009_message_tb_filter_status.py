# Generated by Django 2.1.7 on 2021-08-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_trash_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_tb',
            name='filter_status',
            field=models.CharField(default=1, max_length=20),
        ),
    ]
