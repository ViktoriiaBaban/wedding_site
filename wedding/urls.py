from .views import *
from django.urls import path

urlpatterns = [
    path('', guests_attend),
    path('guests/', AllGuests.as_view())
]