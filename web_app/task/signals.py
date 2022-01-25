

def my_callback(sender, **kwargs):
    from .tasks import run_crawler

    if kwargs.get("created"):
        instance = kwargs.get("instance")
        if instance.task_name == "run_crawler":
            run_crawler.delay(instance.id)
