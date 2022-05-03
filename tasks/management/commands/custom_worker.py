from django.conf import settings
from django.core.management.base import BaseCommand

import django_rq, os
from rq import Queue, Worker
from rq_win import WindowsWorker


def my_handler(job, *exc_info):
    print("FAILURE")
    print(job)
    print(exc_info)


class Command(BaseCommand):
    def handle(self, *args, **options):
        redis_conn = django_rq.get_connection('default')
        
        q = Queue(connection=redis_conn)
        if os.name == 'nt':
            worker = WindowsWorker([q], exc_handler=my_handler, connection=redis_conn)
        else:
            worker = Worker([q], exc_handler=my_handler, connection=redis_conn)
        worker.work()