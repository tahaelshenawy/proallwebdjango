"""prowebsloutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path ,include
#MEDIA
from django.conf import settings
from django.conf.urls.static import static
from ar.sitemaps import postSitemap
from en.sitemaps import postSitemaps
from django.contrib.sitemaps.views import sitemap
sitemaps={
    
    'posts':postSitemap,
    'posts2':postSitemaps,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemaps.xml/',sitemap,{'sitemaps':sitemaps}), 
    path('',include('ar.url')),
    path('',include('en.url')),
    path('',include('accounts.url')),
     #Sitemap
    
] 




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#handler404 = "ar.views.handler404"
#handler500 = 'ar.views.handler500'
#handler403 = 'ar.views.handler403'
#handler400 = 'ar.views.handler400'