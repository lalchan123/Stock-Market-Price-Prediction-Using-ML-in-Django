from django.db import models
from django.db.models.fields import DecimalField

# Create your models here.
class StockPredict(models.Model):
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()
    pre_price_close = models.FloatField()
   