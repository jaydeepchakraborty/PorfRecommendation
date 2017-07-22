from recoprofconst import *

output_list = [
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lsa_kclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lsa_hclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lda_kclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lda_hclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/hdp_kclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/hdp_hclust_op.csv"]

gold_copy = "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/gold_copy.csv"

#-------------------------------------calAcc START----------------------------------------
def calAcc():

    y_true = []
    with open(gold_copy, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if row[4].strip() == "Y":
                y_true.append(1)
            else:
                y_true.append(0)

    #print(y_true)
    count = len(output_list)
    
    for i in range(0, count):
        output_file = output_list[i]
        y_pred = []
        try:
            with open(output_file, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                next(reader)
                for row in reader:
                    if row[1].strip() == "Y":
                        y_pred.append(1)
                    else:
                        y_pred.append(0)
            
            #print(y_pred)
            print("--------------"+output_file+"--------------")        
            print("F1 score:- "+str(f1_score(y_true, y_pred, average='binary')))
            print("Precision score:- "+str(precision_score(y_true, y_pred,  average='binary')))
            print("Recall score:- "+str(recall_score(y_true, y_pred, average='binary')))
            print("Accuracy score:- "+str(accuracy_score(y_true, y_pred))) 
            #print("Cohen Kappa score:- "+str(cohen_kappa_score(y_true, y_pred)))
            print(confusion_matrix(y_true, y_pred))  
            #in binary classification, the count of 
            #true negatives is C_{0,0} and false positives is C_{0,1}
            #false negatives is C_{1,0} and true positives is C_{1,1}. 
        except:
            traceback.print_exc()
#-------------------------------------calAcc STOP----------------------------------------


calAcc()



print("---END---")
