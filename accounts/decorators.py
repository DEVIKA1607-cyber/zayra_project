from django.core.exceptions import PermissionDenied

def role_required(required_role):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == required_role:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return wrapper
    return decorator
