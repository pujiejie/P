from rest_framework import serializers
from .models import Owner, License


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    owner_id = LicenseSerializer(many=True, read_only=True)

    class Meta:
        # 指定序列化对应的模型
        model = Owner
        fields = ['name', 'home_number', 'owner_id']
