from .models import Owner
from rest_framework.viewsets import ModelViewSet
from .serializers import OwnerSerializer


class OwnerView(ModelViewSet):
    """
    用户详情数据API接口表
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


