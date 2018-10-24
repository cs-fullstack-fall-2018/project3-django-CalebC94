from django.db import models
from django.contrib.auth.models import User


class Expenses(models.Model):
    emergencyFund = models.IntegerField()
    checking = models.IntegerField()
    timeAccountCreated = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __int__(self):
        return self.emergencyFund

class Transaction(models.Model):
    name = models.CharField(max_length=100)
    amount =models.IntegerField()
    timeOfTransaction = models.DateTimeField()
    account = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name