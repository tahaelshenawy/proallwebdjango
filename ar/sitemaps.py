from django.contrib.sitemaps import Sitemap
from .models import Pages

class postSitemap(Sitemap):
    def items(self):
        return Pages.objects.all()