'''
This file is for generating similar professor
'''
from recoprofconst import *
from sklearn.cluster.hierarchical import AgglomerativeClustering

lsa_csv = prof_topic_matrix_path+"lsa-topic-matrix.csv"
lda_csv = prof_topic_matrix_path+"lda-topic-matrix.csv"
hdp_csv = prof_topic_matrix_path+"hdp-topic-matrix.csv"

def reduceDimension(prof_data,prof_nm_lst_np,figure_nm):
    #pca  = PCA(0.72)#I want 95% data is to be preserved
    #print(pca.n_components_)
    pca  = PCA(2)#project to @ D data
    reduced_data = pca.fit_transform(prof_data)
    
    reduced_data_np = np.array(reduced_data)
    dim_1 = reduced_data_np[:,0]
    dim_2 = reduced_data_np[:,1]
    plt.figure(figure_nm)
    plt.scatter(dim_1,dim_2)
#     for i, txt in enumerate(prof_nm_lst_np):
#         plt.annotate(txt,(dim_1[i],dim_2[i]))
    plt.show()
     

def predictClusterIndex(prof_data,prof_nm_lst_np):
   normalized_prof_data = preprocessing.normalize(prof_data)
   standardized_prof_data = preprocessing.scale(prof_data)
   
   reduceDimension(prof_data,prof_nm_lst_np,'actual')
   reduceDimension(normalized_prof_data,prof_nm_lst_np,'normalized')
   reduceDimension(standardized_prof_data,prof_nm_lst_np,'standardized')

   indices = pairwise_distances(prof_data,metric='cosine')
  # print(indices)
   return indices
   


def func_us_knn():
    try: 
        prof_data = np.genfromtxt(hdp_csv, delimiter=',')
       
        
        prof_nm_lst = []
        for prof in open(prof_lst_file_nm,'rt', encoding='latin1'):
                prof_nm_lst.append("".join(prof.split()))
        
     
        prof_nm_lst_np = np.array(prof_nm_lst)
        preds = predictClusterIndex(prof_data,prof_nm_lst_np)
        for pred in preds:
            print(pred)
            np_pred = np.argsort(np.array(pred))[:6]
            print(np_pred)
            for pred_val in np_pred:
                print(prof_nm_lst[pred_val] + " -- ")
            print('\n')
    except:
        traceback.print_exc()

func_us_knn()   

print("---END---")

