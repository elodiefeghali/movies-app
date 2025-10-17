
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Video
from .forms import VideoForm

# Read (list)
def video_list(request):
    q = request.GET.get("q", "")
    videos = Video.objects.all().order_by("-ReleaseYear", "MovieTitle")
    if q:
        videos = videos.filter(MovieTitle__icontains=q)
    return render(request, "videos/video_list.html", {"videos": videos, "q": q})

# Read (detail)
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, "videos/video_detail.html", {"video": video})

# Create
def video_create(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save()
            return redirect(reverse("videos:detail", args=[video.pk]))  # PRG
    else:
        form = VideoForm()
    return render(request, "videos/video_form.html", {"form": form, "mode": "Create"})

# Update
def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect(reverse("videos:detail", args=[video.pk]))  # PRG
    else:
        form = VideoForm(instance=video)
    return render(request, "videos/video_form.html", {"form": form, "mode": "Update", "video": video})

# Delete
def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == "POST":
        video.delete()
        return redirect("videos:list") 
    return render(request, "videos/video_confirm_delete.html", {"video": video})
