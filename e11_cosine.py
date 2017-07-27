from recoprofconst import *
import plotly.plotly as py


csv_file_nm = "/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim/LDA_KCLUST_OP.csv"
prof_nm_lst = []

try:
    for prof in open("faculty_list.txt",'rt', encoding='utf8'):
        prof_nm_lst.append("".join(prof.split()))
    total_prof_num = len(prof_nm_lst)
    
    csv_file = pd.read_csv(csv_file_nm)
    prof_data = csv_file.iloc[:, 1:16]
    #print(prof_data)
    
    dist_prof = pairwise_distances(prof_data,metric='cosine')
    #print(dist_prof[0])
    
#     plt.hist(dist_prof[2], bins='auto')
#     plt.title("Gaussian Histogram")
#     plt.xlabel("Value")
#     plt.ylabel("Frequency")
#     
#     plt.show()

    #distance 0-1, o is most similar and 1 is most dissimilar
    for upper_threshold in range(1,9,1):
        upper_threshold = upper_threshold / 10 #steps should be 0.1, 0.2,0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9
        csv_op_fl_nm = "lda_cosine_op" + str(upper_threshold*10) + ".csv"
        with open(csv_op_fl_nm, 'w+') as out:
            writer = csv.writer(out)
            writer.writerow(["id", "value"])
            for outer_num in range(0,total_prof_num):
                dist_row = dist_prof[outer_num]
                for inner_num in range(outer_num+1,total_prof_num):
                    if 0< dist_row[inner_num] < (upper_threshold + 0.01):
                        row = [prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num],"Y"]
                    else:
                        row = [prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num],"N"]
                    writer.writerow(row)
    
    
    for upper_threshold in range(5,60,5): #steps should be 5,10,15,20,25,30,35,40,45,50,55,60
        csv_op_fl_nm = "lda_cosine2_op" + str(upper_threshold) + ".csv"
        with open(csv_op_fl_nm, 'w+') as out:
            writer = csv.writer(out)
            writer.writerow(["id", "value"])
            for outer_num in range(0,total_prof_num):
                dist_row = dist_prof[outer_num]
                np_pred = np.argsort(np.array(dist_row))[:upper_threshold]
                for inner_num in range(outer_num+1,total_prof_num):
                    if inner_num in np_pred:
                        row = [prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num],"Y"]
                    else:
                        row = [prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num],"N"]
                    writer.writerow(row)    
       
except:
    traceback.print_exc()
#-------------------------------------STOP----------------------------------------

print("---END---")