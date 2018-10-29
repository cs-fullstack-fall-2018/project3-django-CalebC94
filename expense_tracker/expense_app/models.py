from django.db import models
from django.contrib.auth.models import User


class Expenses(models.Model):
    emergencyFund = models.IntegerField()
    balance = models.IntegerField()
    timeAccountCreated = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __int__(self):
        return self.emergencyFund

class Account(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()


