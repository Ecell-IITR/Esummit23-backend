"""esummit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
import public.urls as publicUrls
import design.urls as designUrls
import user.urls as userUrls
import events.urls as eventsUrls
import CAP.urls as capurls
import ticket.urls as ticketUrls
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('public/', include(publicUrls)),
    path('design/', include(designUrls)),
    path('user/', include(userUrls)),
    path("rq/", include('django_rq.urls')),
    path('events/', include(eventsUrls)),
    path('cap/', include(capurls)),
    path('ticket/', include(ticketUrls)),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
