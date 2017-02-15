# @Author: Chen yunsheng(Leo YS CHen)
# @Location: Taiwan
# @E-mail:leoyenschen@gmail.com
# @Date:   2017-02-14 00:11:27
# @Last Modified by:   Chen yunsheng

from django.shortcuts import render,render_to_response
from django.template import RequestContext
import sys
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,Http404,HttpResponseRedirect
import json
from time import time
import random

# Create your views here.
def hello_world(request):
    return render_to_response('hello_world.html',{},context_instance = RequestContext(request))


@csrf_exempt
def highchart_run(request):
    print("leo test highchart_run")
    #print(request.POST)
    x = time() * 1000
    y = random.randint(0,99)

    return HttpResponse(json.dumps([x,y]), content_type="application/json")
        #return render_to_response('strategy_run.html', locals())
