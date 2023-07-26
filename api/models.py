from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100, null=False)
    moneyPaid = models.IntegerField(null=False)

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    name = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=True)

    buyers = models.ManyToManyField(Buyer, related_name='purchases', blank=True)
    
    def __str__(self):
        return self.name