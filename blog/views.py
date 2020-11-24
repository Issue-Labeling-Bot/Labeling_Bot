from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

import json,requests
import Executor as ex




@csrf_exempt
def post_list(request):

    jsondata = request.body
    
    return HttpResponse("pong")


ex.setData(jsondata)
