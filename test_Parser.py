import json

with open('first.json', 'r') as f1:
    json_data1 = json.load(f1)


with open('second.json', 'r') as f2:
    json_data2 = json.load(f2)


def parsing(json_data):
    label_existence = False
    d = json.loads(json_data)
    state = d['action']
    issues = d['issue']        
    title = issues['title']
    body = issues['body']
    label = issues['labels']
    number = issues['number']

    if label:
        label_existence = True
   
    return state, title, body, number, label_existence

def test_pasing1():
    state, title, body, number, label_existence = parsing(json_data1)
    
    assert state == 'opened'
    assert title == 'I want go home'
    assert body == 'Not here'
    assert number == 8
    assert label_existence == False


def test_pasing2():
    state, title, body, number, label_existence = parsing(json_data2)
    
    assert state == 'opened'
    assert title == 'Hello world'
    assert body == 'Bye Bye'
    assert number == 7
    assert label_existence == False
