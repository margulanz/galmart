from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import RecordedOrder
from .serializers import RecordedOrderSerializer

# Система учета
class RecordedOrderViewSet(viewsets.ModelViewSet):
    queryset = RecordedOrder.objects.all()
    serializer_class = RecordedOrderSerializer
    #permission_classes = (permissions.IsAuthenticated, )
