import json
import requests
from classifier import Classifier
from dbConnector import DBConnector

class IssueProcessor:
    def attach_label(self, data, access_token=None):
        issue = data['issue']
        repository = issue['repository_url'] ## full_name
        title = issue['title']
        body = issue['body']
        number = issue['number']
        labels = []
        
        if access_token is None:
            access_token = DBConnector().loadAccessToken(repository)

        if not labels:
            labels = Classifier().predict(title, body)
            url = '{}/issues/{}/labels'.format(repository, number)
            header = {'Authorization': 'token {}'.format(access_token), 'Accept': 'application/vnd.github.v3+json'}
            data = json.dumps({'labels': labels})
            print(access_token)
            print(url)
            print(data)
            response = requests.post(url, headers=header, data=data)
        else:
            pass
