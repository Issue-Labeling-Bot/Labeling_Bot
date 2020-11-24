from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

import json,requests

from github3 import login


@csrf_exempt
def post_list(request):

    jsondata = request.body
    
    d = json.loads(jsondata)
    state = d['action']
    issues = d['issue']
    token='226e5d255cccfa18c305402f63e5d91d33082c3e'
    title = issues['title']
    body = issues['body']
    label = issues['labels']
    number = issues['number']
    print(number)
    if state == "opened":
        gh = login('Issue-Labeling-Bot', password='quf**2266')
        gh = login(token=token)
        issue = gh.issue('Issue-Labeling-Bot','Labeling_Bot', number)      
        issue.add_labels('enhancement')
        issue.add_labels('bug')
        
    return HttpResponse("pong")
