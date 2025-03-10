from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from apps.transactions.models import Transaction
from apps.utils.permissions import is_librarian


@login_required(login_url="login")
@is_librarian
def get_transactions(request, *args, **kwargs):
    transaction_list = Transaction.objects.all()
    paginator = Paginator(transaction_list, 20)
    page_number = request.GET.get("page")
    transactions = paginator.get_page(page_number)

    return render(request, "transactions.html", {"transactions": transactions})


@login_required(login_url="login")
@is_librarian
def get_transaction(request, *args, **kwargs):
    transaction_id = kwargs.get("transaction_id")
    transaction = Transaction.objects.filter(id=transaction_id).first()

    return render(
        request,
        "transaction_detail.html",
        {"transaction": transaction},
    )
