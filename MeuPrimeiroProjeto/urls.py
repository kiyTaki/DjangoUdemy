
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from .views import hello, articles, fname2

from clientes import urls as clients_urls


urlpatterns = [
    path('hello/', hello),
    path('articles/<int:year>/', articles),
    path('pessoa/<str:nome>/', fname2),
    path('person/', include(clients_urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

