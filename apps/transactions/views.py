from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages

from apps.transactions.models import Transaction
from apps.utils.permissions import is_librarian
from apps.transactions.forms import TransactionForm


@login_required(login_url="login")
@is_librarian
def get_transactions(request, *args, **kwargs):
    transaction_list = Transaction.objects.all()
    paginator = Paginator(transaction_list, 15) # paginate by transaction
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


@login_required(login_url="login")
@is_librarian
def update_transaction(request, *args, **kwargs):
    # Update the transaction object
    transaction_id = kwargs.get("transaction_id")
    transaction = Transaction.objects.filter(id=transaction_id).first()
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            transaction.book.available_copies = transaction.book.available_copies + 1
            transaction.book.save()
            messages.success(request, "Transaction updated successfully!")
            return redirect("transactions")
        else:
            messages.error(request, "Failed to update transaction!")
            return redirect("transactions")
            
    form = TransactionForm(instance=transaction)
    return render(
        request,
        "update_transaction.html",
        {"form": form, "transaction": transaction},
    )
