import json

class Parser:
    
    def parsing(json_data):
        label_existence = False
        d = json.loads(json_data)
        state = d['action']
        issues = d['issue']        
        title = issues['title']
        body = issues['body']
        label = issues['labels']
        number = issues['number']

        Classifier(title, body)

        if label:
            label_existence = True
   

        return state, title, body, number, label_existence
            
        
