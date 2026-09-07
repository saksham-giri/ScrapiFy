from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from listings.models import Scrap
from django.contrib.auth import authenticate, login, logout
from listings.forms import *

def register(request):
    if request.method== "POST":
        form = RegistrationUser(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("login")
        
    else:
        form=RegistrationUser()

    return render(request,"register.html",{"form":form})

def user_login(request):
    if request.method=="POST":
        form=LoginUser(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password"]
            
            user=authenticate(
                request,
                username=username,
                password=password)
            
            if user is not None:
                login(request, user)
                
                if user.role=="seller":
                    return redirect("seller_dashboard")
                
                return redirect("buyer_dashboard")
        
    else: form=LoginUser()    
    return render(request,"login.html",{"form":form})
        
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
    
    my_listings = Scrap.objects.filter(
        seller=request.user
    )

    context = {
        "my_listings": my_listings,
        "total_listings":my_listings.count()
    }

    return render(
        request,
        "seller.html",
        context
    )
    

@login_required
def buyer_dashboard(request):
    if request.user.role != "buyer":
        return redirect("seller_dashboard")
    return render(request, "buyer.html")

@login_required
def ScrapDetails(request, pk):
    detailedlisting=Scrap.objects.get(id=pk)
    
    return render(request, "scrapdetails.html",{"detailedlisting": detailedlisting})

@login_required
def edit_listing(request, pk):
    listing=Scrap.objects.get(id=pk)
    
    if request.method=="POST":
        form=ScrapForm(request.POST, instance=listing)
        
        if form.is_valid():
            form.save()
            return redirect("seller_dashboard")
        
    else:
        form=ScrapForm(instance=listing)
        
    return render(request,"edit.html",{"form":form})

@login_required
def delete_listing(request, pk):
    listing=Scrap.objects.get(id=pk)
    
    listing.delete()
    
    return redirect("seller_dashboard")