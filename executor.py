##import json
from github3 import login
from information import Info

class Executor:
    def __init__(self, json_data):
        info = Info(json_data)
        number = info.getNumber()
        
        if info.getState() == "opened":

            token='226e5d255cccfa18c305402f63e5d91d33082c3e'

            gh = login(token=token)
            issue = gh.issue('Issue-Labeling-Bot','Labeling_Bot', number)      
            issue.add_labels('enhancement')
            issue.add_labels('bug')
    

