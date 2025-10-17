from django.urls import path
from . import views

app_name = "videos"

urlpatterns = [
    path("", views.video_list, name="list"),
    path("<int:pk>/", views.video_detail, name="detail"),
    path("new/", views.video_create, name="create"),
    path("<int:pk>/edit/", views.video_update, name="update"),
    path("<int:pk>/delete/", views.video_delete, name="delete"),
]
