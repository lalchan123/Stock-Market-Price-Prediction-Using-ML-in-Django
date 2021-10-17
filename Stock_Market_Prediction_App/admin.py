from django.contrib import admin
from .models import StockPredict
# Register your models here.
class StockPredictAdmin(admin.ModelAdmin):
    list_display = ('open','high','low','volume','pre_price_close')
    list_filter = ('pre_price_close',)

admin.site.register(StockPredict,StockPredictAdmin)
