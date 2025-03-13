from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from apps.notifications.models import Notification
from apps.utils.permissions import is_member, is_librarian


@login_required
@is_member
def get_notifications(request, *args, **kwargs):
    notification_list = Notification.objects.filter(
        recipient=request.user, is_read=False
    ).order_by("-created_at")

    paginator = Paginator(notification_list, 15)
    page_number = request.GET.get("page")
    notifications = paginator.get_page(page_number)

    return render(request, "notifications.html", {"notifications": notifications})


@login_required
@is_member
def update_notification(request, *args, **kwargs):
    notification_id = kwargs.get("notification_id")
    notification = Notification.objects.filter(id=notification_id).first()
    if notification is None:
        messages.error(request, "Notification not found.")
        return redirect("notifications")

    notification.is_read = True
    notification.save()
    messages.success(request, "Notification marked as read.")
    return redirect("notifications")
