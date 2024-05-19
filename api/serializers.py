from .models import Buyer, Purchase
from rest_framework.serializers import ModelSerializer

class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class BuyerSerializer(ModelSerializer):
    purchases = PurchaseSerializer(read_only=True, many=True)

    class Meta:
        model = Buyer
        fields = ['id', 'name', 'moneyPaid', 'purchases']
