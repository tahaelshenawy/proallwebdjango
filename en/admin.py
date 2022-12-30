from django.contrib import admin
from .models import EnPages, UploadLogos,tempaltes,Socia,footerOne,footerTwo,footerThree,Login
# Register your models here.



admin.site.register(EnPages)

class PageAdmin(admin.ModelAdmin):
    list_display =('titel','update_date')
    ordering = ('titel',)
    search_fields= ('titel',)

admin.site.register(UploadLogos)
admin.site.register(tempaltes)


admin.site.register(Socia)
  

admin.site.register(footerOne)
admin.site.register(footerTwo)
admin.site.register(footerThree)
admin.site.register(Login)

