##import json
from github3 import login
from information import Info
<<<<<<< HEAD
=======
from classifier import Classifier
>>>>>>> Classifier

class Executor:
    def __init__(self, json_data):
        info = Info(json_data)
        number = info.getNumber()
        
        if info.getState() == "opened":

<<<<<<< HEAD
            token='226e5d255cccfa18c305402f63e5d91d33082c3e'

            gh = login(token=token)
            issue = gh.issue('Issue-Labeling-Bot','Labeling_Bot', number)      
            issue.add_labels('enhancement')
            issue.add_labels('bug')
=======
            cl = Classifier
            labels = cl.classify(info.getTitle(), info.getBody())

            token='8f80028ae8308e73ce27bf46af3c0569f4004087'

            gh = login(token=token)
            issue = gh.issue('Choi-kwang-hyun','webhook_test', number)
            
            for i in range(len(labels)):
                issue.add_labels(labels[i])
>>>>>>> Classifier
    

