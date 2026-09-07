from django.shortcuts import redirect
from django.urls import path


def home(request):
    if request.user.is_authenticated:
        return redirect("seller_dashboard" if request.user.role == "seller" else "buyer_dashboard")
    return redirect("login")


urlpatterns = [path("", home, name="home")]
