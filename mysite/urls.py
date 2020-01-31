from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('business/', include('business.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
