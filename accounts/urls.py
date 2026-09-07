from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path("register/", register, name="register"),
    # path("login/",LoginView.as_view(template_name="login.html"), name="login"),
    path("profile/", profile , name="profile"),
    path("seller_dashboard/", seller_dashboard, name="seller_dashboard" ),
    path("buyer_dashboard/", buyer_dashboard, name="buyer_dashboard" ),
    path("login/", user_login, name="login"),
    path("logout/", logout_view, name="logout"),
    path("scrapdetails/<int:pk>", ScrapDetails, name="scrapdetails"),
    path("<int:pk>/edit_listing/", edit_listing, name="edit_listing"),
    path("<int:pk>/delete_listing/", delete_listing, name="delete_listing"),
]
