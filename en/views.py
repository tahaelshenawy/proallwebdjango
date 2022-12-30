from django.shortcuts import render ,get_object_or_404
from .models import EnPages,UploadLogos,footerOne ,footerTwo ,footerThree,Login
from .forms import loginForm
# Create your views here.


def enindex(request ,pagename,):
    
    try:
      pagename ='/en/'+ pagename
      pg = EnPages.objects.get(permalink=pagename)
    except EnPages.DoesNotExist:
      pg =  get_object_or_404(EnPages, pk=1)
     
    imglogo =UploadLogos.objects.get()
    footer =footerOne.objects.all()
    footer2 =footerTwo.objects.all()
    footer3 =footerThree.objects.all()
   
    context = {
           'titel':pg.titel,
           'content':pg.bodytext,
           'last_updated':pg.update_date,
           'page_list':EnPages.objects.all(),
           'description':pg.meta_description,
           'keywords':pg.meta_keywords,
           'imglogos':imglogo.image,
           'title_footer':footer,
           'title_footer2':footer2,
           'title_footer3':footer3,
          

    }   
   
   
    #assert False  
    tempaltes='theme_en/pages/index-en.html'
    return render(request,tempaltes,context)




def test(request):
   if request.method == 'POST':
      usernamepage = request.POST.get('username')
      passwordpage = request.POST.get('password')
      date =Login(username=usernamepage,password=passwordpage)
      date.save()

      tempaltes='theme_en/pages/test.html'
      return render(request,tempaltes,{'lf':loginForm})
   else:
    tempaltes='theme_en/pages/test.html'
    return render(request,tempaltes,{'lf':loginForm})
    
     






    
    

