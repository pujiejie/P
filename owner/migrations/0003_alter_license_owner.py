# Generated by Django 4.0.5 on 2022-06-01 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_alter_license_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carlist', to='owner.owner'),
        ),
    ]
