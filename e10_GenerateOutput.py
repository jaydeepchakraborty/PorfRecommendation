from recoprofconst import *


op_fl_list = [  "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/LSA_KCLUST_OP.csv",
                "lsa.data.km.cluster",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lsa_kclust_op.csv",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/LDA_KCLUST_OP.csv",
                "lda.data.km.cluster",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lda_kclust_op.csv",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/HDP_KCLUST_OP.csv",
                "hdp.data.km.cluster",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/hdp_kclust_op.csv",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/LSA_HCLUST_OP.csv",
                "lsa.data.op",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lsa_hclust_op.csv",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/LDA_HCLUST_OP.csv",
                "lda.data.op",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/lda_hclust_op.csv",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/HDP_HCLUST_OP.csv",
                "hdp.data.op",
                "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/output/hdp_hclust_op.csv" ]

count = len(op_fl_list)
    
for i in range(0, count,3):

    csv_file_nm = op_fl_list[i]
    csv_col_nm = op_fl_list[i+1]
    csv_op_fl_nm = op_fl_list[i+2]
    
    prof_nm_lst = []
    
    try:
        for prof in open(prof_lst_file_nm,'rt', encoding='utf8'):
                prof_nm_lst.append("".join(prof.split()))
                
        
        total_prof_num = len(prof_nm_lst)
        
        
        csv_file = pd.read_csv(csv_file_nm)
        op_col = csv_file[csv_col_nm]
    
        
        with open(csv_op_fl_nm, 'w+') as out:
            writer = csv.writer(out)
            writer.writerow(["id", "value"])
            for outer_num in range(0,total_prof_num):
                for inner_num in range(outer_num+1,total_prof_num):
                    if op_col[outer_num] == op_col[inner_num]:
                        row = [prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num],"Y"]
                    else:
                        row = [prof_nm_lst[outer_num] + "--" + prof_nm_lst[inner_num],"N"]
                    writer.writerow(row)
            
        
    except:
        traceback.print_exc()
#-------------------------------------STOP----------------------------------------

print("---END---")
