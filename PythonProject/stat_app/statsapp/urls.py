from django.urls import path
from .views import run_stats

urlpatterns = [
    path("", run_stats, name="run_stats"),
]
