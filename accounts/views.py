from django.shortcuts import render
from ar.models import Pages, UploadLogos, footerOne ,footerTwo ,footerThree,Socia,menu
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
   # form = UserCreationForm()

    imglogo =UploadLogos.objects.get()
    footer =footerOne.objects.all()
    footer2 =footerTwo.objects.all()
    footer3 =footerThree.objects.all()
    socail= Socia.objects.get()
   
  
         
    context = {
           'form':UserCreationForm(),
           #'page_list':Pages.objects.all(),
           'page_list':menu.objects.all(),
           'imglogos':imglogo.image,
           'title_footer':footer,
           'title_footer2':footer2,
           'title_footer3':footer3,
           'Socia_facebook':socail.facebook,
           'socail_twitter':socail.twitter,
           'socail_linkedin':socail.linkedin,
           'socail_youtube':socail.youtube,
           'title_footer_li_link':footer,
          

    }  

    return render(request,'themebase/pages/signup.html',context)
