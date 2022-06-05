from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    salt = models.CharField(max_length=100)
    tem = models.CharField(max_length=20)
    pic = models.ImageField(upload_to='images/', null=True)

    def check_password(self):
        print(self.password)
        return True
