# أستدعاء مكتبة الفورم من داخل مكتبة الديجانجو 
from django import forms
from django.forms import ModelForm
from .models import Login 

# تم أنشاء كلاس لوجن فورم من المكتبه فورمز فورم
#داخل الكلاس تم أنشاء متغيران يوزنيم وباس ورد
# نفس المتغيران   بنفس القيم  يتم أنشاء مثلهم داخل الموديلز فى الداتا بيز مره أخرى 
#الأختلاف فى المتغيران  عن  الموديلز هما أنك تستدعى المكتبه فورمز بدل  موديلز 

class LoginForms(forms.Form):
    username =forms.CharField(max_length=50,label="Username taha", initial="Enter username")
    password =forms.CharField(max_length=50,widget=forms.PasswordInput,label="Password", initial="password")



class JobForm(ModelForm):
    class Meta:
        model = Login
        fields = ['username','password' ]
        
        
        
        
class ContactForm(forms.Form):
	name = forms.CharField(max_length = 50)
	email= forms.EmailField(max_length = 150)
	subject = forms.CharField(widget = forms.Textarea, max_length = 2000)        
        
        
        
        
        
        
