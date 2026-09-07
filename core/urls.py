from django.shortcuts import redirect, render
from django.urls import path


def home(request):
    if request.user.is_authenticated:
        return redirect("seller_dashboard" if request.user.role == "seller" else "buyer_dashboard")
    return render(request, "home.html")


urlpatterns = [path("", home, name="home")]
