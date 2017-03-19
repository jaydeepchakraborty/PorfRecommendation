'''
This file is for generating similar professor
'''
from recoprofconst import *

prof_nm_lst = []
for prof in open(prof_lst_file_nm,'rt', encoding='latin1'):
    prof_nm_lst.append("".join(prof.split()))


lsa_arr = []
with open(prof_topic_dist_path +"lsa-topic-dist.txt", 'r', encoding='latin-1') as prof_dist_file:
        for line in prof_dist_file:
            line_arr = line.replace("\n","").replace(")","").replace("]","").split(",")[2::2]
            line_tmp_arr = np.array(line_arr, dtype='|S4')
            line_float_arr = line_tmp_arr.astype(np.float)
            lsa_arr.append(line_float_arr)

lsa_tmp_arr =  np.array(lsa_arr)
lsa_sparse = sparse.csr_matrix(lsa_tmp_arr)

lsa_sim = cosine_similarity(lsa_sparse)
#print('pairwise LSA dense output:\n {}\n'.format(lsa_sim))

for lsa_sim_tmp in lsa_sim:
    sim_prof_lst = lsa_sim_tmp.argsort()[-6:][::-1] #It will fetch top 5 professor
    #print(sim_prof_lst)
    print(str(prof_nm_lst[sim_prof_lst[0]]) + "---> "+ str(prof_nm_lst[sim_prof_lst[1]]) + ", " + str(prof_nm_lst[sim_prof_lst[2]]) + ", " + str(prof_nm_lst[sim_prof_lst[3]]) + ", " + str(prof_nm_lst[sim_prof_lst[4]]) + ", " + str(prof_nm_lst[sim_prof_lst[5]]))
    
print("---END---")

