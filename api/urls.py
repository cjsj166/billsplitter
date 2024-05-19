from django.urls import path, include
from . import views

urlpatterns = [
    path('buyers/', views.getBuyers ,name='getBuyers'),
    path('purchases/', views.getPurchases, name='getPurchases'),
    path('buyers/<str:pk>', views.updateBuyer ,name='updateBuyer'),
    path('purchases/<str:pk>', views.updatePurchase ,name='updatePurchase'),
    path('buyers/<str:pk>/updateRelation', views.updatePurchaseRelation ,name='updatePurchaseRelation'),
]
