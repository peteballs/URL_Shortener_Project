from django.urls import path
from . import views

urlpatterns = [
    path('', views.make, name = 'make_new'),
    path('<slug:url>', views.redirector, name = 'redirector'),
]