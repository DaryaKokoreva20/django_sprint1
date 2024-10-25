from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('about/', include('pages.urls', namespace='pages')),
    path('admin/', admin.site.urls),
]
