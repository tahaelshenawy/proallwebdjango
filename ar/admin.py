from django.contrib import admin

from .models import Login, Pages,UploadLogos, Socia,footerOne,footerThree,footerTwo,contect_us,menu
# Register your models here.
admin.site.site_header = 'Pro All Web'
admin.site.site_title = 'Pro All Web'
admin.site.index_title = 'Pro All Web Administration'

class PageAdmin(admin.ModelAdmin):
    list_display =('titel','update_date')
    ordering = ('titel',)
    search_fields= ('titel',)

admin.site.register(Login)
admin.site.register(Pages, PageAdmin)

admin.site.register(UploadLogos)
admin.site.register(Socia)
admin.site.register(menu)  

admin.site.register(footerOne)
admin.site.register(footerTwo)
admin.site.register(footerThree)
admin.site.register(contect_us)



