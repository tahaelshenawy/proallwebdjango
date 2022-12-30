from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.


class EnPages(models.Model):
    titel = models.CharField(max_length=68)
    #Meta Begin
    meta_titel = models.CharField(max_length=68,blank=True)
    meta_description = models.CharField('description',max_length=160,blank=True)
    meta_keywords = models.CharField('keywords',max_length=160,blank=True)
    #Meta end
    permalink = models.CharField(max_length=12, unique= True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = RichTextField('Page Content', blank=True)

    def __str__(self):
         return self.titel

    def get_absolute_url(self):
       return reverse('enindex', args=[str(self.titel)])  
     
     

      
      
class tempaltes(models.Model):
  
    tempaltes_url = models.CharField(max_length=1000, blank=True)  
    

class UploadLogos(models.Model):  
       caption = models.CharField(max_length=200)  
       image = models.ImageField(upload_to='images')  
  
       def __str__(self):  
          return self.caption            
      
      
      
      
      
class Socia(models.Model):
    
       facebook = models.CharField(max_length=1000, blank=True)
       twitter = models.CharField(max_length=1000,blank=True)
       linkedin = models.CharField(max_length=1000,blank=True)
       youtube = models.CharField(max_length=1000,blank=True)

       def __str__(self):  
         return self.linkedin  
     
     
     
class footerOne(models.Model):
    #box_footer
       title_footer_h4 = models.CharField(max_length=68, blank=True,unique=True)
       
       title_footer_li_link = models.CharField(max_length=68, blank=True,unique=True)
       li_link_footer = models.CharField(max_length=68, blank=True)
       
       def __str__(self):  
         return self.title_footer_h4        
     


class footerTwo(models.Model):
    #box_footer
         main_footer_h4 = models.CharField(max_length=68, blank=True)
         title_footer_h4 = models.CharField(max_length=68, blank=True)
       
         title_footer_li_link = models.CharField(max_length=68, blank=True)
         li_link_footer = models.CharField(max_length=68, blank=True)
       
         def __str__(self):  
           return self.title_footer_h4   
       
       
class footerThree(models.Model):
    #box_footer
         main_footer_h4 = models.CharField(max_length=68, blank=True)
         title_footer_h4 = models.CharField(max_length=68, blank=True)
       
         title_footer_li_link = models.CharField(max_length=68, blank=True)
         li_link_footer = models.CharField(max_length=68, blank=True)
       
         def __str__(self):  
           return self.title_footer_h4   


class Login(models.Model):
  username = models.CharField(max_length=50,null=True, blank=True)
  password = models.CharField(max_length=50,null=True, blank=True)      
 
  
class contect_us(models.Model):
           
     name = models.CharField(max_length=200,null=True, blank=True)
     email = models.EmailField(null=True, blank=True)
     subject = models.TextField(null=True, blank=True)
     
     def __str__(self):  
          return self.name  
           