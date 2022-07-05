from django.shortcuts import redirect


class LoginAuthenticateMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:login")
        return super(LoginAuthenticateMixin, self).dispatch(request, *args, **kwargs)
