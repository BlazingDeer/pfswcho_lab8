from django.urls import path
from . import views

urlpatterns = [path("", views.fib_seqView, name="index")]
