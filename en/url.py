from django.urls import path 
from . import views
#Sitemap
#from .sitemaps import postSitemap
#from django.contrib.sitemaps.views import sitemap


urlpatterns = [
    path ('en/', views.enindex, {'pagename': ''}, name='enindex'),
    path('en/<str:pagename>', views.enindex, name='enindex'),
    path('test/',views.test,),
     #Sitemap
  
   

]

#handler404='en.view.error_404_view'