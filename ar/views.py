from typing_extensions import Self
from django.shortcuts import render,get_object_or_404,HttpResponse, redirect
from django.core.mail import send_mail, BadHeaderError


from .forms import ContactForm

# جلب الكلاس لوجن من  صفحة الداتا بيز
from .models import Pages, UploadLogos, footerOne ,footerTwo ,footerThree,Socia,contect_us,menu



def index(request ,pagename):
    
    try:
      pagename ='/'+ pagename
      pg = Pages.objects.get(permalink=pagename)
    except Pages.DoesNotExist:
      pg =  get_object_or_404(Pages, pk=1)
    
    imglogo =UploadLogos.objects.get()
    footer =footerOne.objects.all()
    footer2 =footerTwo.objects.all()
    footer3 =footerThree.objects.all()
    socail= Socia.objects.get()
   
  
         
    context = {
           'titel':pg.titel,
           'content':pg.bodytext,
           'last_updated':pg.update_date,
           #'page_list':Pages.objects.all(),
           'page_list':menu.objects.all(),
           'permalink':pg.permalink,
           'description':pg.meta_description,
           'keywords':pg.meta_keywords,
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

    #assert False    
    tempaltes='themebase/pages/index.html'
    return render(request,tempaltes,context)
   
      
   # return render (request,'themebase/pages/contct.html',context)
def thank_you(request):
    template = 'themebase/pages/thank_you.html'
    context = {}
    return render(request, template, context)   
   
def contect(request):
    
    
    imglogo =UploadLogos.objects.get()
    footer  =footerOne.objects.all()
    footer2 =footerTwo.objects.all()
    footer3 =footerThree.objects.all()
    socail  =Socia.objects.get()
         
    context = {
           
           'page_list':menu.objects.all(),
           'permalink':Pages.permalink,
           'imglogos':imglogo.image,
           'title_footer':footer,
           'title_footer2':footer2,
           'title_footer3':footer3,
           'Socia_facebook':socail.facebook,
           'socail_twitter':socail.twitter,
           'socail_linkedin':socail.linkedin,
           'socail_youtube':socail.youtube,
           

    }  
   # contect=contect_us()
    if request.method == 'POST':

       name=request.POST.get('name')
       email=request.POST.get('email')
       subject=request.POST.get('subject')
       data=contect_us(name=name,email=email,subject=subject)
       data.save()
      
       return render(request, 'themebase/pages/thank_you.html',context)

    else:   

      return render(request, 'themebase/pages/contct.html',context)








