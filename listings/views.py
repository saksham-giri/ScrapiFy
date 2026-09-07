from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from listings.models import *
from .forms import *

@login_required
def ScrapListing(request):
    if request.method=="POST":
        form=ScrapForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.seller = request.user
            listing.save()
            return redirect("seller_dashboard")
    else :
        form=ScrapForm()
    
    return render(request,"createlisting.html",{"form":form})

@login_required
def marketplace(request):
    if request.user.role!="buyer":
        return redirect("seller_dashboard")
    else:
        listings=Scrap.objects.filter(status='available')
    
        return render(request, "marketplace.html",{"listings":listings})