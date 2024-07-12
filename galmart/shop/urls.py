from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecordedOrderViewSet

router = DefaultRouter()
router.register(r'', RecordedOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]