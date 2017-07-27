from recoprofconst import *

output_list = [
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lsa_kclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lda_kclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/hdp_kclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lsa_hclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lda_hclust_op.csv",
    "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/hdp_hclust_op.csv"]

gold_copy = "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/feedback/gold_copy.csv"

#-------------------------------------calAcc START----------------------------------------
def calAcc():

    y_true = []
    with open(gold_copy, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        for row in reader:
            if row[6].strip() == "Y":#0,1,2,3,4,5,6 --> 6 is GOLD
                y_true.append(1)
            else:
                y_true.append(0)

    #print(y_true)
    count = len(output_list)
    
    for i in range(0, count, 3):
        lsa_output_file = output_list[i]
        lda_output_file = output_list[i+1]
        hdp_output_file = output_list[i+2]
        lsa_y_pred = []
        lda_y_pred = []
        hdp_y_pred = []
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        precision = dict()
        recall = dict()
        try:
            with open(lsa_output_file, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                next(reader)
                for row in reader:
                    if row[1].strip() == "Y":
                        lsa_y_pred.append(1)
                    else:
                        lsa_y_pred.append(0)
            
            
            with open(lda_output_file, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                next(reader)
                for row in reader:
                    if row[1].strip() == "Y":
                        lda_y_pred.append(1)
                    else:
                        lda_y_pred.append(0)
                        
            
            with open(hdp_output_file, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                next(reader)
                for row in reader:
                    if row[1].strip() == "Y":
                        hdp_y_pred.append(1)
                    else:
                        hdp_y_pred.append(0)
            
            print("--------------"+lsa_output_file+"--------------")        
            print("F1 score:- "+str(f1_score(y_true, lsa_y_pred, average='binary')))
            print("Precision score:- "+str(precision_score(y_true, lsa_y_pred,  average='binary')))
            print("Recall score:- "+str(recall_score(y_true, lsa_y_pred, average='binary')))
            print("Accuracy score:- "+str(accuracy_score(y_true, lsa_y_pred)))
            print("V measure score:- "+str(v_measure_score(y_true, lsa_y_pred)))
            print("Adjusted Rand Index:- "+str(adjusted_rand_score(y_true, lsa_y_pred)))
            #print("Cohen Kappa score:- "+str(cohen_kappa_score(y_true, y_pred)))
            print(confusion_matrix(y_true, lsa_y_pred))  
            #in binary classification, the count of 
            #true negatives is C_{0,0} and false positives is C_{0,1}
            #false negatives is C_{1,0} and true positives is C_{1,1}. 
            
            print("--------------"+lda_output_file+"--------------")        
            print("F1 score:- "+str(f1_score(y_true, lda_y_pred, average='binary')))
            print("Precision score:- "+str(precision_score(y_true, lda_y_pred,  average='binary')))
            print("Recall score:- "+str(recall_score(y_true, lda_y_pred, average='binary')))
            print("Accuracy score:- "+str(accuracy_score(y_true, lda_y_pred))) 
            #print("Cohen Kappa score:- "+str(cohen_kappa_score(y_true, y_pred)))
            print("V measure score:- "+str(v_measure_score(y_true, lda_y_pred)))
            print("Adjusted Rand Index:- "+str(adjusted_rand_score(y_true, lda_y_pred)))
            print(confusion_matrix(y_true, lda_y_pred))  
            #in binary classification, the count of 
            #true negatives is C_{0,0} and false positives is C_{0,1}
            #false negatives is C_{1,0} and true positives is C_{1,1}.
            
            
            print("--------------"+hdp_output_file+"--------------")        
            print("F1 score:- "+str(f1_score(y_true, hdp_y_pred, average='binary')))
            print("Precision score:- "+str(precision_score(y_true, hdp_y_pred,  average='binary')))
            print("Recall score:- "+str(recall_score(y_true, hdp_y_pred, average='binary')))
            print("Accuracy score:- "+str(accuracy_score(y_true, hdp_y_pred)))
            print("V measure score:- "+str(v_measure_score(y_true, hdp_y_pred))) 
            print("Adjusted Rand Index:- "+str(adjusted_rand_score(y_true, hdp_y_pred)))
            #print("Cohen Kappa score:- "+str(cohen_kappa_score(y_true, y_pred)))
            print(confusion_matrix(y_true, hdp_y_pred))  
            #in binary classification, the count of 
            #true negatives is C_{0,0} and false positives is C_{0,1}
            #false negatives is C_{1,0} and true positives is C_{1,1}.
            
            fpr[1], tpr[1], thresholds = roc_curve(y_true, lsa_y_pred)
            roc_auc[1] = auc(fpr[1], tpr[1])
            print("ROC curve"+str(roc_auc[1]))
            plt.plot(fpr[1],tpr[1],color='darkorange', label='ROC curve (area = %0.2f)' % roc_auc[1])
            plt.legend(loc="lower right")
            
            
            fpr[2], tpr[2], thresholds = roc_curve(y_true, lda_y_pred)
            roc_auc[2] = auc(fpr[2], tpr[2])
            print("ROC curve"+str(roc_auc[2]))
            plt.plot(fpr[2],tpr[2],color='navy', label='ROC curve (area = %0.2f)' % roc_auc[2])
            plt.legend(loc="lower right")
            
            fpr[3], tpr[3], thresholds = roc_curve(y_true, hdp_y_pred)
            roc_auc[3] = auc(fpr[3], tpr[3])
            print("ROC curve"+str(roc_auc[3]))
            plt.plot(fpr[3],tpr[3],color='red', label='ROC curve (area = %0.2f)' % roc_auc[3])
            plt.legend(loc="lower right")
            
            
            plt.show() 
            
            
            precision[1], recall[1], thresholds = precision_recall_curve(y_true, lsa_y_pred)
            plt.plot(precision[1],recall[1],color='darkorange')
            
            precision[2], recall[2], thresholds = precision_recall_curve(y_true, lda_y_pred)
            plt.plot(precision[2],recall[2],color='navy')
            
            precision[3], recall[3], thresholds = precision_recall_curve(y_true, hdp_y_pred)
            plt.plot(precision[3],recall[3],color='red')
            
            plt.show()
            
            
        except:
            traceback.print_exc()
#-------------------------------------calAcc STOP----------------------------------------


calAcc()



print("---END---")
