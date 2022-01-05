from django.contrib.sitemaps import Sitemap
from .models import Article, Project

class ArticleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.created

