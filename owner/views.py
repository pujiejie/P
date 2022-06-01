from .models import Owner, License
from rest_framework.viewsets import ModelViewSet
from .serializers import OwnerSerializer, LicenseSerializer


class OwnerView(ModelViewSet):
    """
    用户详情数据API接口表
    """
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class LicenseView(ModelViewSet):
    """
    用户车辆API
    """
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
