import re
import django.db.utils
from rest_framework import serializers
from .models import Users
from django.contrib.auth.hashers import make_password
import uuid


class UsersModelSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20, required=True)
    password = serializers.CharField(max_length=20, required=True)
    tem = serializers.CharField(max_length=20, required=True)
    pic = serializers.ImageField()

    class Meta:
        model = Users
        fields = ['username', 'password']

    def validate_password(self, pwd):
        if not re.search(r'^\w{6,18}$', pwd):
            raise serializers.ValidationError("密码长度最少6位最多18位")
        return pwd

    def validate_tem(self, tem):
        if not re.search(r'^\d{11}$', tem):
            raise serializers.ValidationError("手机号格式错误，只支持11位手机号")
        return tem

    def create(self, request):
        _uuid = uuid.uuid1().hex
        try:
            user = Users.objects.create(
                username=self.data.get('username'),
                password=make_password(self.data.get('password'), _uuid),
                tem=self.data.get('tem'),
                salt=_uuid,
                pic=request.data.get('pic')
            )
            return UsersModelSerializer(instance=user).data
        except django.db.utils.IntegrityError:
            raise serializers.ValidationError({
                'username': '账户名已存在'
            })
