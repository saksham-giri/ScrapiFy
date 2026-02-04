from django.urls import path

from . import views


urlpatterns = [
	path("", views.landing, name="landing"),
	path("auth/buyer/", views.buyer_auth, name="buyer_auth"),
	path("auth/seller/", views.seller_auth, name="seller_auth"),
	path("dashboard/buyer/", views.buyer_dashboard, name="buyer_dashboard"),
	path("dashboard/seller/", views.seller_dashboard, name="seller_dashboard"),
	path("dashboard/admin/", views.admin_dashboard, name="admin_dashboard"),
]
