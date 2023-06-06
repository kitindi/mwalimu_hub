from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.urls import path, include
from schools.views import home, jobboard, jobdetails, posts

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("jobs/", jobboard, name="jobs"),
    path("job/<int:id>", jobdetails, name="job"),
    path("blog/", posts, name="blog"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

# add this lines


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
