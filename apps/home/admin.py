from django.contrib import admin

# Register your models here.

from .models import Series, Transaction, StrategyDeck, StrategyCard

# admin.site.register(User)

admin.site.register(Series)
admin.site.register(Transaction)

admin.site.register(StrategyDeck)
admin.site.register(StrategyCard)