##import json
from github3 import login
from information import Info

from Classifier import Classifier


class Executor:
    def __init__(self, json_data):

        info = Info(json_data)
        number = info.getNumber()
        token='226e5d255cccfa18c305402f63e5d91d33082c3e'

        if self.isOpened(info) == True:
            if self.is_there_label(info) == False:
                cl = Classifier
                labels = self.classify(info, cl)
                self.labeling(labels, token, number)


    def isOpened(self, info):
        state = False

        if info.getState() == "opened":
            state = True
        return state


    def classify(self, info, cl):
        labels = cl.classify(info.getTitle(), info.getBody())
        return labels


    def labeling(self, labels, token, number):

        gh = login(token=token)
        issue = gh.issue('Issue-Labeling-Bot','Labeling_Bot', number)
            
        for i in range(len(labels)):
            issue.add_labels(labels[i])
        

    def is_there_label(self, info):
        if info.getLabel_existence() == True:
            return True
        return False
    
        

    

