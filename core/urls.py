from django.urls import path
from core.views import home, no_permission, features, pricing, about, contact

urlpatterns = [
    path('', home, name='home'),
    path('no-permission/', no_permission, name='no-permission'),
    path('features/', features, name='features'),
    path('pricing/', pricing, name='pricing'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]