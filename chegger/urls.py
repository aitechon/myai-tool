from django.urls import path
from .views import generate_answer_view

urlpatterns = [path("", generate_answer_view, name="home")]
