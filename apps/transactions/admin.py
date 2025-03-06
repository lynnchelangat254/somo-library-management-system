from django.contrib import admin

from apps.transactions.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "borrow_date",
        "return_date",
        "status",
    )
    list_per_page = 20


admin.site.register(Transaction, TransactionAdmin)
