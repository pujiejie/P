from django.urls import path, include
from rest_framework import routers
from .views import OwnerView

router = routers.DefaultRouter()
router.register(r'owner', OwnerView)

urlpatterns = [
    path('', include(router.urls))
]