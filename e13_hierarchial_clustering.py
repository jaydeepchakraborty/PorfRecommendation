'''
This file is for generating similar professor
'''
from recoprofconst import *
from sklearn.cluster.hierarchical import AgglomerativeClustering

lsa_csv = prof_topic_matrix_path+"lsa-topic-matrix.csv"
lda_csv = prof_topic_matrix_path+"lda-topic-matrix.csv"
hdp_csv = prof_topic_matrix_path+"hdp-topic-matrix.csv"
num_cluster = 6

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
    
    
def plotScores(prof_data):

    k_range = range(2,25)#As we have 25 professors
    silhouette_scores = []
    calinski_harabaz_scores = []
    for k in k_range:
        hc = AgglomerativeClustering(n_clusters=k,linkage='ward')
        pred_cluster = hc.fit_predict(prof_data)
        
        
        #Compute the mean Silhouette Coefficient of all samples.
        #The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters.
        #Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.
        silhouette_scores.append(silhouette_score(prof_data,pred_cluster))
        
    N = len(silhouette_scores)
    x = range(N)
    width = 1/1.5
    plt.bar(x, silhouette_scores, width)
    plt.xticks(x, k_range)
    plt.ylabel('Silhouette Scores')
    plt.title('Silhouette Scores vs K')
    plt.show() 


def plotVornoi(prof_data):
    
    pca  = PCA(2)#project to @ D data
    reduced_data = pca.fit_transform(prof_data)
    
    reduced_data = np.array(reduced_data)
    
    hc = AgglomerativeClustering(n_clusters=num_cluster,linkage='ward')
    pred_cluster = hc.fit_predict(prof_data)
    
    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].
    
    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
    
    # Obtain labels for each point in mesh. Use last trained model.
    Z = hc.fit_predict(np.c_[xx.ravel(), yy.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')
    
    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
 
    plt.title('Hierarchical clustering on the digits dataset (PCA-reduced data)\n'
              )
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()



def predictClusterIndex(prof_data,prof_nm_lst_np):
    normalized_prof_data = preprocessing.normalize(prof_data)
    standardized_prof_data = preprocessing.scale(prof_data)
   
    plotScores(normalized_prof_data)
   
    plotVornoi(normalized_prof_data)
    
    hierar_clust = AgglomerativeClustering(n_clusters=num_cluster)
    pred_cluster = hierar_clust.fit_predict(normalized_prof_data)
    
#     ii = itertools.count(normalized_prof_data.shape[0])
#     s = [{'node_id':next(ii), 'left':x[0], 'right':x[1]} for x in hierar_clust.children_]
#     
#     pp = pprint.PrettyPrinter(indent=4)
#     pp.pprint(s)
   
    return pred_cluster
   


def func_hierarchical_clust():
    try: 
        prof_data = np.genfromtxt(hdp_csv, delimiter=',')
       
        
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

func_hierarchical_clust()   

print("---END---")

