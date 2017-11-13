from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(R'^admin/', admin.site.urls),
    url(R'', include('blog.urls')),
]

