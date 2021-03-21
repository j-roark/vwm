from django.contrib import admin
from django.urls import path
from .views import Index
from django.conf import settings
from django.conf.urls.static import static
from items.views import Categories
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index),
    path('Category/<str:url_category>/', Categories)
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print(urlpatterns)
