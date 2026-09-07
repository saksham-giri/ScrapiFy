from django.contrib.auth.decorators import login_required
from django.db import IntegrityError, transaction
from django.shortcuts import get_object_or_404, redirect, render
from listings.models import Booking, Scrap
from .forms import ScrapForm


@login_required
def ScrapListing(request):
    if request.user.role != "seller":
        return redirect("buyer_dashboard")
    form = ScrapForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        listing = form.save(commit=False)
        listing.seller = request.user
        listing.save()
        return redirect("seller_dashboard")
    return render(request, "createlisting.html", {"form": form})


@login_required
def marketplace(request):
    if request.user.role != "buyer":
        return redirect("seller_dashboard")
    listings = Scrap.objects.filter(status="available").select_related("seller").order_by("-created_at")
    return render(request, "marketplace.html", {"listings": listings})


@login_required
def book_listing(request, pk):
    if request.user.role != "buyer":
        return redirect("seller_dashboard")
    listing = get_object_or_404(Scrap, pk=pk, status="available")
    if request.method == "POST":
        try:
            with transaction.atomic():
                listing = Scrap.objects.select_for_update().get(pk=pk, status="available")
                Booking.objects.create(scrap=listing, buyer=request.user)
                listing.status = "not available"
                listing.save(update_fields=["status"])
        except (Scrap.DoesNotExist, IntegrityError):
            pass
    return redirect("buyer_dashboard")
