from Parser import Parser

class Info:

    def __init__(self, json_data):
        parser = Parser
        self.state, self.title, self.body, self.issuenumber, self.label_existence = parser.parsing(json_data)
        print(self.state)
        
    def getState(self):
        return self.state

    def getNumber(self):
        return self.issuenumber

    def getTitle(self):
        return self.title

    def getBody(self):
        return self.body

    def getLabel_existence(self):
        return self.label_existence
