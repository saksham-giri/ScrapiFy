from  django.urls import path
from .views import *
urlpatterns = [
    path("list/",ScrapListing, name="ScrapListing"),
    path("marketplace/", marketplace, name="marketplace")
]
