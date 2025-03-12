from apps.members.models import Member
from apps.librarians.models import Librarian
from apps.utils.permissions import is_librarian
from apps.members.forms import MemberForm

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from datetime import datetime


@login_required(login_url="login")
@is_librarian
def get_members(request, *args, **kwargs):
    # Fetch all objects from the model
    member_list = Member.objects.filter(membership_status="Approved")
    # paginate the list
    paginator = Paginator(member_list, 15)
    page_number = request.GET.get("page")
    members = paginator.get_page(page_number)

    return render(request, "members.html", {"members": members})


@login_required(login_url="login")
@is_librarian
def get_member(request, *args, **kwargs):
    member_id = kwargs.get("member_id")
    member = Member.objects.filter(id=member_id).first()
    # check if the member exists in the database
    if member is None:
        messages.error(request, "Member not found.")
        return redirect("members")
    return render(request, "member_detail.html", {"member": member})


@login_required(login_url="login")
@is_librarian
def update_member(request, *args, **kwargs):
    # Update an existing member in the database by id
    member_id = kwargs.get("member_id")
    member = Member.objects.get(id=member_id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, "Member updated successfully!")
            return redirect("members")

    form = MemberForm(instance=member)
    return render(request, "update_member.html", {"form": form})


@login_required(login_url="login")
@is_librarian
def delete_member(request, *args, **kwargs):
    # Delete a member from the database by id
    member_id = kwargs.get("member_id")
    member = Member.objects.filter(id=member_id).first()
    # check if the member exists in the database
    if member is None:
        messages.error(request, "Member not found.")
        return redirect("members")
    member.delete()
    messages.success(request, "Member deleted successfully!")
    return redirect("members")


@login_required(login_url="login")
@is_librarian
def get_membership_requests(request, *args, **kwargs):
    # Fetch all membership requests from the model
    membership_requests = Member.objects.filter(membership_status="Pending")
    # paginate the list
    paginator = Paginator(membership_requests, 15)
    page_number = request.GET.get("page")
    requests = paginator.get_page(page_number)
    return render(request, "membership_requests.html", {"requests": requests})


@login_required(login_url="login")
@is_librarian
def approve_membership_request(request, *args, **kwargs):
    # Process a membership request
    member_id = kwargs.get("member_id")
    member = Member.objects.filter(id=member_id).first()
    # check if the member exists in the database
    if member is None:
        messages.error(request, "Member not found.")
        return redirect("membership-requests")
    if member.membership_status == "Pending":
        member.membership_status = "Approved"
        member.approval_date = datetime.now()
        member.approved_by = Librarian.objects.filter(user=request.user).first()
        # update member role
        member.user.role = "Member"
        member.user.save()
        member.save()
        messages.success(request, "Membership request processed successfully!")
    else:
        messages.error(request, "Membership request is already processed.")
    return redirect("membership-requests")


@login_required(login_url="login")
@is_librarian
def decline_membership_request(request, *args, **kwargs):
    # Process a membership request
    member_id = kwargs.get("member_id")
    member = Member.objects.filter(id=member_id).first()
    # check if the member exists in the database
    if member is None:
        messages.error(request, "Member not found.")
        return redirect("membership-requests")
    if member.membership_status == "Pending":
        member.membership_status = "Declined"
        member.save()
        messages.success(request, "Membership request declined successfully!")
    else:
        messages.error(request, "Membership request is already processed.")
    return redirect("membership-requests")
