import fasttext

class Classifier:

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

        
