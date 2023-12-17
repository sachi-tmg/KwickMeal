from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your existing URL patterns go here
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)