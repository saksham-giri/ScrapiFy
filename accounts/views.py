from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import LoginUser, RegistrationUser
from listings.models import Booking, Scrap


def register(request):
    form = RegistrationUser(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("login")
    return render(request, "register.html", {"form": form})


def user_login(request):
    form = LoginUser(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])
        if user is not None:
            login(request, user)
            return redirect("seller_dashboard" if user.role == "seller" else "buyer_dashboard")
        form.add_error(None, "Invalid username or password.")
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def profile(request):
    return render(request, "profile.html")


@login_required
def seller_dashboard(request):
    if request.user.role != "seller":
        return redirect("buyer_dashboard")
    my_listings = Scrap.objects.filter(seller=request.user).order_by("-created_at")
    pending_pickups = Booking.objects.filter(scrap__seller=request.user, status__in=["pending", "confirmed"]).count()
    completed_pickups = Booking.objects.filter(scrap__seller=request.user, status="completed").count()
    return render(request, "seller.html", {"my_listings": my_listings, "total_listings": my_listings.count(), "pending_pickups": pending_pickups, "completed_pickups": completed_pickups})


@login_required
def buyer_dashboard(request):
    if request.user.role != "buyer":
        return redirect("seller_dashboard")
    bookings = Booking.objects.filter(buyer=request.user).select_related("scrap", "scrap__seller").order_by("-booked_at")
    return render(request, "buyer.html", {"bookings": bookings, "active_bookings": bookings.filter(status__in=["pending", "confirmed"]).count(), "completed_bookings": bookings.filter(status="completed").count()})


@login_required
def ScrapDetails(request, pk):
    detailedlisting = get_object_or_404(Scrap, pk=pk)
    return render(request, "scrapdetails.html", {"detailedlisting": detailedlisting})


@login_required
def edit_listing(request, pk):
    listing = get_object_or_404(Scrap, pk=pk, seller=request.user)
    from listings.forms import ScrapForm
    form = ScrapForm(request.POST or None, instance=listing)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("seller_dashboard")
    return render(request, "edit.html", {"form": form})


@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Scrap, pk=pk, seller=request.user)
    if request.method != "POST":
        return render(request, "confirm_delete.html", {"listing": listing})
    listing.delete()
    return redirect("seller_dashboard")
