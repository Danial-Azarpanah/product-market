from django.shortcuts import redirect


class LoginAuthenticateMixin:
    """
    This mixin is for authenticating whether user is logged in or not
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:login")
        return super(LoginAuthenticateMixin, self).dispatch(request, *args, **kwargs)
