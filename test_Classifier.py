import fasttext

title1 = 'Add plugin interface for renaming an unsaved tab'
body1 = 'Notepad++ version 7.6.4 (I think) introduced the capability to rename an unsaved tab. For example, a tab with the title \"new 2" can be right-clicked upon, \"Rename" chosen from the resulting popup menu, and the following box presents image What is needed is a way for a plugin to be able to effect this sort of rename, directly, without the popup input box shown above. [ Comments above based upon features available current to Notepad++ 7.9 ]'

title2 = 'Element already has context attribute'
body2 = 'Steps to Reproduce: yarn web reveal output panel => 🐛 Element already has context attribute'

def classify(title, body):

        total_precision_sum = 0
        total_recall_sum = 0
        total_f1_score = 0

        count_precision = 0
        count_recall = 0

        pred_line_count = 0
        recall_line_count = 0

        text = title + ' ' + body.replace('\n', ' ')

        model = fasttext.load_model('./model_cooking.bin')

        ##레이블 추출
        labels = model.predict(text, k=2, threshold=0.1)
        ## labels : __label__bug, __label__enhancement

        re_precision = total_precision_sum/10
        re_recall = total_recall_sum/10
        re_f1_score = total_f1_score/10

        label_list = list((labels))
        label_list = list((label_list[0]))
        print(label_list)
        for i in range(len(label_list)):
            label_list[i] = label_list[i].replace('__label__', '')
            print(label_list[i])

        
        
        return label_list

def test_classifier1():
    result1 = ['featurerequest', 'duplicate']
    assert classify(title1, body1) == result1

def test_classifier2():
    result2 = ['verified', 'bug']
    assert classify(title2, body2) == result2
