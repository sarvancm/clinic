import functools
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse


def customer_not(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_user:
            messages.warning(request, 'permision denied')
            return redirect('login_view')
        else:
            return view_func(request,*args, **kwargs)
    return wrapper