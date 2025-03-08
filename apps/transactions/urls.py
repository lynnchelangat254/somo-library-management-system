from apps.transactions import views

from django.urls import path


urlpatterns = [
    path("librarian/transactions/", views.get_transactions, name="transactions"),
    path(
        "librarian/transactions/<str:transaction_id>/",
        views.get_transaction,
        name="transaction-detail",
    ),
]
