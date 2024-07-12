from rest_framework import serializers
from .models import RecordedOrder

class RecordedOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecordedOrder
        fields = "__all__"