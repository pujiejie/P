# Generated by Django 4.0.5 on 2022-06-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0005_alter_owner_park_lot_alter_owner_park_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='car_img',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
