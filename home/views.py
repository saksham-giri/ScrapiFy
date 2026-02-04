from django.http import HttpResponseForbidden
from django.shortcuts import render


def landing(request):
	return render(request, "landing.html")


def buyer_auth(request):
	return render(request, "auth_buyer.html")


def seller_auth(request):
	return render(request, "auth_seller.html")


def buyer_dashboard(request):
	if not request.user.is_authenticated:
		return render(request, "auth_buyer.html")
	if not request.user.groups.filter(name="Buyer").exists():
		return HttpResponseForbidden("Buyer access required.")
	return render(request, "dashboard_buyer.html")


def seller_dashboard(request):
	if not request.user.is_authenticated:
		return render(request, "auth_seller.html")
	if not request.user.groups.filter(name="Seller").exists():
		return HttpResponseForbidden("Seller access required.")
	return render(request, "dashboard_seller.html")


def admin_dashboard(request):
	if not request.user.is_authenticated:
		return HttpResponseForbidden("Admin access required.")
	if not request.user.is_staff:
		return HttpResponseForbidden("Admin access required.")
	return render(request, "dashboard_admin.html")
