from django.http import HttpResponse
from .permissions import can_create_post

def create_permission_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not can_create_post(request.user):
            return HttpResponse("Permission Denied", status=403)
        return view_func(request, *args, **kwargs)
    return wrapper