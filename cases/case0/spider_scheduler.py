#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""APScheduler

Advanced Python Scheduler (APScheduler) is a Python library
that lets you schedule your Python code to be executed later, either just once or periodically.

APScheduler has three built-in scheduling systems
- Cron-style scheduling (with optional start/end times)
- Interval-based execution (runs jobs on even intervals, with optional start/end times)
- One-off delayed execution (runs jobs once, on a set date/time)

Your choice of scheduler depends mostly on your programming environment and
what you’ll be using APScheduler for.
Here’s a quick guide for choosing a scheduler:
- BlockingScheduler: use when the scheduler is the only thing running in your process
- BackgroundScheduler: use when you’re not using any of the frameworks below,
    and want the scheduler to run in the background inside your application
- AsyncIOScheduler: use if your application uses the asyncio module

When you schedule a job, you need to choose a trigger for it.
The trigger determines the logic by which the dates/times are calculated when the job will be run.
APScheduler comes with three built-in trigger types:
- date: use when you want to run the job just once at a certain point of time
- interval: use when you want to run the job at fixed intervals of time
- cron: use when you want to run the job periodically at certain time(s) of day

Adding jobs
- by calling add_job()
- by decorating a function with scheduled_job()
The first way is the most common way to do it. The second way is mostly a convenience to declare jobs
that don’t change during the application’s run time.
The add_job() method returns a apscheduler.job.Job instance
that you can use to modify or remove the job later.

add_job()
- add_job(task, 'interval', weeks=0, hours=0, minutes=0, seconds=0, start_date=None, end_date=None, timezone=None, jitter=None)
- add_job(task, 'cron', year=None, month=None, day=None, week=None, day_of_week=None, hour=None, minute=None, second=None, start_date=None, end_date=None, timezone=None, jitter=None)
    - year (int|str) – 4-digit year
    - month (int|str) – month (1-12)
    - day (int|str) – day of the (1-31)
    - week (int|str) – ISO week (1-53)
    - day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
    - hour (int|str) – hour (0-23)
    - minute (int|str) – minute (0-59)
    - second (int|str) – second (0-59)
    - start_date (datetime|str) – earliest possible date/time to trigger on (inclusive)
    - end_date (datetime|str) – latest possible date/time to trigger on (inclusive)
    - timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone)
    - jitter (int|None) – advance or delay the job execution by jitter seconds at most.
- add_job(task, 'date', run_date=None, timezone=None)

实现定时爬虫任务
- 使用APScheduler库
- 利用操作系统提供的能力，如 Windows task scheduler
"""

from apscheduler.schedulers.blocking import BlockingScheduler
import time


# 模拟爬虫任务
def spider_task():
    print('Crawl at', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


if __name__ == '__main__':
    scheduler = BlockingScheduler()

    # 间隔任务 - 每过十分钟执行一次
    # scheduler.add_job(say_hello, 'interval', minutes=10)

    # 定时任务 - 周一到周五的中午12点半执行
    scheduler.add_job(spider_task, 'cron', day_of_week='mon-fri', hour=12, minute=30)

    # 在某个特定时间点执行的一次性任务
    # scheduler.add_job(spider_task, 'date', run_date='2020-11-11 00:00:00')

    scheduler.start()
