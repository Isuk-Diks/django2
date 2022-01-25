from django.db import models
from threading import Thread
from news.crawlers import hacker_crawler

CHOICES = (("run_crawler", "Run Crawler"),)


class Task(models.Model):
    task_name = models.CharField(max_length=255, choices=CHOICES)
    started = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

    def save(self, *args, **kwargs):
        if not self.done:
            Thread(target=hacker_crawler.crawl_site, args=(self, )).start()
            self.status = "task started"
        return super().save(*args, **kwargs)