from django.contrib import admin

# Register your models here.

from .models import Filter, Note, TransactionSeries, Transaction, StrategyDeck, StrategyCard

# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

# admin.site.register(User)

# class StrategyCardResource(resources.ModelResource):
#     class Meta:
#         model = StrategyCard
# class StrategyCardAdmin(ImportExportModelAdmin):
#     resource_class = StrategyCardResource


admin.site.register(TransactionSeries)
admin.site.register(Transaction)

admin.site.register(StrategyDeck)

admin.site.register(StrategyCard)
# admin.site.register(StrategyCardAdmin)

admin.site.register(Note)
admin.site.register(Filter)