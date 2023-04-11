from django.contrib import admin
from .models import Purchase, Item


admin.site.register(Item)


class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'item', 'date_purchase']


admin.site.register(Purchase)




