from django import forms


from apps.transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["fine_amount", "status"]

    fine_amount = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter Fine Amount"}
        ),
        min_value=0,
        decimal_places=2,
        max_digits=6,
    )

    status = forms.ChoiceField(
        choices=Transaction.TransactionStatus,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
