from django.urls import path
from . import views

app_name = "videos"

urlpatterns = [
    path("", views.video_list, name="list"),
    path("videos/<int:pk>/", views.video_detail, name="detail"),
    path("videos/new/", views.video_create, name="create"),
    path("videos/<int:pk>/edit/", views.video_update, name="update"),
    path("videos/<int:pk>/delete/", views.video_delete, name="delete"),
]

