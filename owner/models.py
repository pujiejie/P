from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=20)
    home_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    # 车位号
    park_lot = models.CharField(max_length=20, default="")
    # 车位状态 0 没有停放车辆 1 已停满
    park_state = models.CharField(max_length=1, default="0")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class License(models.Model):
    license = models.CharField(max_length=20)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="carlist")
    car_img = models.ImageField(upload_to="images/", null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
