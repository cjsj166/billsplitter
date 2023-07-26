from .models import Buyer, Purchase
from rest_framework.serializers import ModelSerializer

class BuyerSerializer(ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'

class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'