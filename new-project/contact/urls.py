from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('email/', views.email, name='email'),
]