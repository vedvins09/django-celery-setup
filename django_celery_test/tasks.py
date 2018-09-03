# Create your tasks here
from __future__ import absolute_import, unicode_literals

from datetime import datetime, timedelta

from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task


@shared_task
def add(x, y):
    print(x+y)
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@periodic_task(run_every=(crontab(minute='*/1')), name="run_every_minute")
def run_every_minute():
    current_date = datetime.now()
    last_date = current_date - timedelta(days=7)
    date = current_date.strftime("%b %d, %Y")
    print(last_date, date)
    return None
