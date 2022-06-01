from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=20)
    home_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class License(models.Model):
    license = models.CharField(max_length=20)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="owner_id")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
