from recoprofconst import *

LSA_KCLUST_OP = "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/LSA_KCLUST_OP.csv"
LSA_KCLUST_COL_NM = "lsa.data.km.cluster"

LDA_KCLUST_OP = "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/LDA_KCLUST_OP.csv"
LDA_KCLUST_COL_NM = "lda.data.km.cluster"

HDP_KCLUST_OP = "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/HDP_KCLUST_OP.csv"
HDP_KCLUST_COL_NM = "hdp.data.km.cluster"


LSA_HCLUST_OP = "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/LSA_HCLUST_OP.csv"
LSA_HCLUST_COL_NM = "lsa.data.op"

LDA_HCLUST_OP = "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/LDA_HCLUST_OP.csv"
LDA_HCLUST_COL_NM = "lda.data.op"

HDP_HCLUST_OP = "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/HDP_HCLUST_OP.csv"
HDP_HCLUST_COL_NM = "hdp.data.op"

csv_file_nm = LSA_KCLUST_OP
csv_col_nm = LSA_KCLUST_COL_NM

prof_nm_lst = []

try:
    for prof in open(prof_lst_file_nm,'rt', encoding='utf8'):
            prof_nm_lst.append("".join(prof.split()))
            
    
    total_prof_num = len(prof_nm_lst)
    
    
    csv_file = pd.read_csv(csv_file_nm)
    op_col = csv_file[csv_col_nm]

    
    for outer_num in range(0,total_prof_num):
        for inner_num in range(outer_num+1,total_prof_num):
            if op_col[outer_num] == op_col[inner_num]:
                print(prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num] + "-- 1")
            else:
                print(prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num] + "-- 0")
        
    
except:
    traceback.print_exc()
#-------------------------------------STOP----------------------------------------

print("---END---")
