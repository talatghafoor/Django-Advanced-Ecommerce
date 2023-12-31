
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar



urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("playground.urls")),
    
] + static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
