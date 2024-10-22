
from django.db import models
from django.contrib import admin
class Bank (models.Model):
 Name=models.CharField(max_length=25)
 Amount=models.IntegerField()
 Income=models.IntegerField()
 Accountnumber=models.IntegerField(primary_key="Accountnumber")
 Securitypin=models.IntegerField()
 Interest=models.IntegerField()
 Collateral=models.CharField(max_length=30)

class BankAdmin(admin.ModelAdmin):
 list_display=('Name','Amount','Income','Accountnumber','Securitypin','Interest','Collateral')
