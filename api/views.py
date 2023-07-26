from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Buyer, Purchase
from .serializers import BuyerSerializer, PurchaseSerializer


# Create your views here.
@api_view(['GET'])
def getBuyers(request):
    buyers = Buyer.objects.all()
    serializer = BuyerSerializer(buyers, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def getPurchases(request):
    purchases = Purchase.objects.all()
    serializer = PurchaseSerializer(purchases, many=True)
    
    return Response(serializer.data)

#--------------------------Buyers--------------------------

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def updateBuyer(request, pk):
    print('----------updateBuyer activated ---------------')
    
    if request.method == 'POST':
        return createBuyer(request, pk)
    
    if request.method == 'PUT':
        return modifyBuyer(request, pk)

    if request.method == 'DELETE':
        return deleteBuyer(request, pk)

# @api_view(['POST'])
def createBuyer(request, pk):
    data = request.data

    print(data)

    buyer = Buyer.objects.create(
        name = data['name'],
        moneyPaid = data['moneyPaid']
    )

    serializer = BuyerSerializer(buyer, many=False)

    return Response(serializer.data)


# @api_view(['PUT'])
def modifyBuyer(request, pk):
    data = request.data
    buyer = Buyer.objects.get(id=pk)
    serializer = BuyerSerializer(buyer, many=False, data=data)

    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    
    return Response(serializer.data)


# @api_view(['DELETE'])
def deleteBuyer(request, pk):
    buyer = Buyer.objects.get(id=pk)
    buyer.delete()
    return Response('Buyer was deleted')

#--------------------------Purchase--------------------------

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def updatePurchase(request, pk):
    print('----------updatePurchase activated ---------------')
    
    if request.method == 'POST':
        return createPurchase(request, pk)
    
    if request.method == 'PUT':
        return modifyPurchase(request, pk)

    if request.method == 'DELETE':
        return deletePurchase(request, pk)

# @api_view(['POST'])
def createPurchase(request, pk):
    data = request.data

    purchase = Purchase.objects.create(
        name = data['name'],
        price = data['price']
    )

    serializer = PurchaseSerializer(purchase, many=False)

    return Response(serializer.data)


# @api_view(['PUT'])
def modifyPurchase(request, pk):
    data = request.data
    purchase = Purchase.objects.get(id=pk)
    serializer = PurchaseSerializer(purchase, many=False, data=data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


# @api_view(['DELETE'])
def deletePurchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    purchase.delete()
    return Response('Purchase was deleted')