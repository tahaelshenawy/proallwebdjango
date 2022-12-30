from django.contrib.sitemaps import Sitemap
from .models import EnPages

class postSitemaps(Sitemap):
    def items(self):
        return EnPages.objects.all()