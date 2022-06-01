from rest_framework import serializers
from .models import Owner, License


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'


class OwnerSerializer(serializers.ModelSerializer):
    carlist = LicenseSerializer(many=True, read_only=True)

    class Meta:
        # 指定序列化对应的模型
        model = Owner
        fields = ['id', 'name', 'home_number', 'phone_number', 'park_lot', 'park_state', 'create_time', 'update_time', 'carlist']
