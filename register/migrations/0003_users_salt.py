# Generated by Django 4.0.5 on 2022-06-05 11:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_remove_users_last_login_alter_users_password_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='salt',
            field=models.CharField(default=uuid.UUID('adb87cd6-e4c1-11ec-948b-4ccc6a830b88'), max_length=40),
        ),
    ]
