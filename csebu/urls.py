from django.urls import path
from csebu import views

urlpatterns = [
    path('', views.homepage, name="homepage")
]

