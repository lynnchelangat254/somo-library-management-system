from django.core.exceptions import PermissionDenied
from functools import wraps

from apps.members.models import Member
from apps.librarians.models import Librarian


def is_member(func):
    """
    Decorator to check if the user has a specific role (group).
    If the user does not have the role, raise a PermissionDenied (403).
    """

    @wraps(func)
    def decorator(request, *args, **kwargs):
        # Check if the user is a member
        if not Member.objects.filter(user=request.user).first():
            raise PermissionDenied  # This will raise a 403 error
        return func(request, *args, **kwargs)

    return decorator


def is_librarian(func):
    """
    Decorator to check if the user has a specific role (group).
    If the user does not have the role, raise a PermissionDenied (403).
    """

    @wraps(func)
    def decorator(request, *args, **kwargs):
        # Check if the user is a librarian
        print(request.user)
        if not Librarian.objects.filter(user=request.user).first():
            raise PermissionDenied  # This will raise a 403 error
        return func(request, *args, **kwargs)  # Call the original view function

    return decorator



