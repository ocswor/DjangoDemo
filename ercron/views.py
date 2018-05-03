# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_cron import CronJobBase, Schedule

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        with open('./test.txt','a+') as f:
            f.write('123')

