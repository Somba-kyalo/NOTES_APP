from django.urls import path
from . import views


urlpatterns = [
    path("summarize/<int:pk>/", views.summarize_note, name="ai_summarize_note"),
]