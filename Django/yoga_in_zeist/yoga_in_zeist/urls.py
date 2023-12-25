from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return render(request, 'yoga_classes/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('', index, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)