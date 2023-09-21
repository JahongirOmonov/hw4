from django.urls import path
from .views import CreateCAR, ListCar, UpdateCar



urlpatterns=[
    path('CreateCAR/', CreateCAR.as_view()),
    path('ListCar/', ListCar.as_view()),
    path('UpdateCar/<int:forid>', UpdateCar.as_view()),
]