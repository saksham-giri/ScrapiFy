from django.urls import path
from .views import ScrapListing, marketplace, book_listing

urlpatterns = [
    path("list/", ScrapListing, name="ScrapListing"),
    path("marketplace/", marketplace, name="marketplace"),
    path("<int:pk>/book/", book_listing, name="book_listing"),
]
