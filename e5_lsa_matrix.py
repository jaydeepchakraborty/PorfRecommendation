'''
This file is for generating similar professor
'''
from recoprofconst import *


lsa_arr = []
with open(prof_topic_dist_path +"lsa-topic-dist.txt", 'r', encoding='latin-1') as prof_dist_file:
        for line in prof_dist_file:
            line_arr = line.replace("\n","").replace(")","").replace("]","").split(",")[2::2]
            line_tmp_arr = np.array(line_arr)
            line_float_arr = line_tmp_arr.astype(np.float)
            lsa_arr.append(line_float_arr)

lsa_np_arr =  np.asarray(lsa_arr)

np.savetxt(prof_topic_matrix_path+"lsa-topic-matrix.csv", lsa_np_arr, delimiter=",")


print("---END---")

