from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import get_object_or_404, redirect
from django.urls import include, path

from recipes.models import ShortLink


def redirect_short_link(request, short_code):
    link = get_object_or_404(ShortLink, short_code=short_code)
    return redirect(f'/recipes/{link.recipe.id}/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('s/<str:short_code>/', redirect_short_link),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
