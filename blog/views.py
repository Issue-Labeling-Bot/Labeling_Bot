from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

from executor import Executor



@csrf_exempt
def post_list(request):
    jsondata = request.body
##    Executor(jsondata)        
    return HttpResponse("pong")



HttpResponse("hello world")
