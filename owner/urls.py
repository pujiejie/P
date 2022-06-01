from django.urls import path, include
from rest_framework import routers
from .views import OwnerView, LicenseView

router = routers.DefaultRouter()
router.register(r'owner', OwnerView)
router.register(r'license', LicenseView)

urlpatterns = [
    path('', include(router.urls))
]