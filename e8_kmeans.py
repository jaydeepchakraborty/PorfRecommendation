'''
This file is for generating similar professor
'''
from recoprofconst import *

lsa_csv = prof_topic_matrix_path+"lsa-topic-matrix.csv"
lda_csv = prof_topic_matrix_path+"lda-topic-matrix.csv"
hdp_csv = prof_topic_matrix_path+"hdp-topic-matrix.csv"
num_cluster = 5

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
   
   standardized_prof_data = preprocessing.scale(prof_data)
   normalized_prof_data = preprocessing.normalize(prof_data)
   
   
   reduceDimension(prof_data,prof_nm_lst_np,'actual')
   reduceDimension(normalized_prof_data,prof_nm_lst_np,'normalized')
   reduceDimension(standardized_prof_data,prof_nm_lst_np,'standardized')
   
   km = KMeans(n_clusters=num_cluster, random_state=0).fit(normalized_prof_data)
   pred_cluster = km.predict(normalized_prof_data)
   
   
   #silhouette score of kmeans clustering
   silhouette_avg = silhouette_score(normalized_prof_data,pred_cluster)
   print("silhouette_avg is --> "+str(silhouette_avg))
   
   return pred_cluster
   


def func_kmeans():
    try: 
        prof_data = np.genfromtxt(hdp_csv, delimiter=',')
        
        print("mean of the data --> "+str(np.mean(np.array(prof_data))))
        print("standard deviation of the data --> "+str(np.std(np.array(prof_data))))
       
        
        prof_nm_lst = []
        for prof in open(prof_lst_file_nm,'rt', encoding='latin1'):
                prof_nm_lst.append("".join(prof.split()))
        
     
        prof_nm_lst_np = np.array(prof_nm_lst)
        pred = predictClusterIndex(prof_data,prof_nm_lst_np)
        for clust_ind in range(num_cluster):
            i, = np.where( pred == clust_ind)
            print("-------------------------In cluster "+str(clust_ind)+"-------------------------")
            print(prof_nm_lst_np[i])
        
        print("--------------------------------------------------")
        print(pred)
    except:
        traceback.print_exc()

func_kmeans()   

print("---END---")

