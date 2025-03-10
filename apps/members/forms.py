from django import forms

from apps.members.models import Member  # Make sure these are imported from your models


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member  # Replace with the actual model name
        fields = "__all__"
