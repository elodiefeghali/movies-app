from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('videos.urls')),            # homepage -> videos list
    # or: path('videos/', include('videos.urls')),
]
