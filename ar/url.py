from django.conf.urls.static import static
from django.urls import path
from . import views
#from django.urls import path, re_path


urlpatterns = [
    path ('', views.index, {'pagename':''}, name='index'),
    path('<str:pagename>', views.index,name='index'),
    path('contcat_us/',views.contect, name='contect'),
   # path("/contact/", views.contact, name="contact"),
    path('thanks/', views.thank_you, name='thank-you'),
   
    
    

]
    

