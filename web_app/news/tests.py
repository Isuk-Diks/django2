from django.test import TestCase
from news.crawlers.hacker_crawler import crawl_site
from .models import Article


class CrawlerTestCase(TestCase):
    def test_run_crawler(self):
        crawl_site()
        articles = Article.objects.all()
        self.assertTrue(len(articles) > 0)
