from recoprofconst import *


csv_file_nm = "/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim/LDA_KCLUST_OP_F.csv"
prof_nm_lst = []

try:
    for prof in open("faculty_list.txt",'rt', encoding='utf8'):
        prof_nm_lst.append("".join(prof.split()))
    total_prof_num = len(prof_nm_lst)
    
    
    csv_file = pd.read_csv(csv_file_nm)
    #prof_data = np.array(csv_file.iloc[:, 1:10])
    prof_data = np.array(csv_file.iloc[:, 1:15])
    #prof_data = np.array(csv_file.iloc[:, 1:20])
    #prof_data_cluster = [[],[],[],[],[],[],[],[],[],[]]
    prof_data_cluster = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    #prof_data_cluster = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    #print(prof_data_cluster)
    threshold = 0.2
    for i in range(0,60):
        row = prof_data[i,]
        for j in range(0,14):#9/14/19 for 10/15/20 cluster
#             print(row[j])
#             print(row[j] > threshold)
            if row[j] > threshold and i not in prof_data_cluster[j]:
                prof_data_cluster[j].append(i)
        
    csv_op_fl_nm = "lda_fuzzy_op.csv"
    with open(csv_op_fl_nm, 'w+') as out:
        writer = csv.writer(out)
        writer.writerow(["id", "value"])
        for outer_num in range(0,total_prof_num):
            for inner_num in range(outer_num+1,total_prof_num):
                ind = False
                for cluster in range(0,len(prof_data_cluster)):
                    if outer_num in prof_data_cluster[cluster] and inner_num in prof_data_cluster[cluster]: 
                        ind = True
                        break
                if ind:
                    row = [prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num],"Y"]
                else:
                    row = [prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num],"N"]
                writer.writerow(row)
except:
    traceback.print_exc()
#-------------------------------------STOP----------------------------------------

print("---END---")