# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from django.template import Context, Template
from django.http import (
    Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect,
)
from django.template import loader
import requests
# Create your views here.

class HomeViews(View):
    def get(self,request):

        html = requests.get(
            'https://mp.weixin.qq.com/s?__biz=MjM5MzAwMTg5MA==&mid=2651318806&idx=1&sn=e97bb1ebd2775f4af5484198dde6a82a&chksm=bd6ef2db8a197bcde923bf66b1dffb214fe42724d20d4233ae0fd5e78f6710f33447471beb92&scene=0#rd')
        content = html.content
        # content = loader.render_to_string(template_name, context, request, using=using)
        return HttpResponse(content)
