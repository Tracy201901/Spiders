"""
apscheduler是基于Quartz的一个Python定时任务框架，实现了Quartz的所有功能，使用起来十分方便
"""

import time
from apscheduler.schedulers.blocking import BlockingScheduler


def first_job():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


def second_job():
    print('This is second job !')


def third_job():
    print('This is third job !')


sched = BlockingScheduler()

# # 每隔10秒钟运行1次
# sched.add_job(func=first_job, trigger='interval', seconds= 10)
# # 每隔1分钟运行1次
# sched.add_job(func=second_job, trigger='interval', minutes = 1)
# # 每隔1分10秒运行1次
# sched.add_job(func=third_job, trigger='interval', minutes= 1, seconds = 10)

# 2019年6月23日15点执行
sched.add_job(func=first_job, trigger='cron', year=2019, month=6, day=23, hour=15)
# 6-9月的23日15点执行
sched.add_job(func=second_job, trigger='cron', month='6-9', day=23,hour=15)
# 15点执行
sched.add_job(func=third_job, trigger='cron', hour=15)

sched.start()

