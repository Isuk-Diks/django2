from __future__ import absolute_import, unicode_literals

from celery import shared_task
from news.crawlers.hacker_crawler import crawl_site


@shared_task
def run_crawler(task_pk=None):
    from .models import Task
    if task_pk:
        task = Task.objects.get(pk=task_pk)
        crawl_site(task)
    crawl_site()
