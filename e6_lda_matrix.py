'''
This file is for generating similar professor
'''
from recoprofconst import *


def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]

lda_arr = []
with open(prof_topic_dist_path +"lda-topic-dist.txt", 'r', encoding='latin-1') as prof_dist_file:
        for line in prof_dist_file:
            line_arr = np.zeros((topics,))
            frst_char_indexes = findOccurences(line,"(");
            last_char_indexes = findOccurences(line,")");
            for ind in range(0,len(frst_char_indexes)):
                frst_ind = frst_char_indexes[ind]
                last_ind = last_char_indexes[ind]
                txt_line_arr = line[frst_ind+1:last_ind]
                tmp_arr = txt_line_arr.split(",")
                arr_index = int(tmp_arr[0])
                arr_value = float(tmp_arr[1].strip())
                line_arr[arr_index] = arr_value
            lda_arr.append(line_arr)

lda_np_arr =  np.asarray(lda_arr)

np.savetxt(prof_topic_matrix_path+"lda-topic-matrix.csv", lda_np_arr, delimiter=",")


print("---END---")