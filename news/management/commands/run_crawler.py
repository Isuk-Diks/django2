from django.core.management.base import BaseCommand, CommandError
from news.crawlers.hacker_crawler import crawl_site


class Command(BaseCommand):
    help = 'Run news crawler'

    def handle(self, *args, **options):
        crawl_site()
