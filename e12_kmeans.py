'''
This file is for generating similar professor
'''
from recoprofconst import *


lsa_csv = prof_topic_matrix_path+"lsa-topic-matrix.csv"
lda_csv = prof_topic_matrix_path+"lda-topic-matrix.csv"
hdp_csv = prof_topic_matrix_path+"hdp-topic-matrix.csv"
num_cluster = 7

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
     

def plotElbow(prof_data):
   
    k_range = range(1,25)#As we have 25 professors
    meandist=[]
    
    for k in k_range:
        model=KMeans(n_clusters=k)
        model.fit(prof_data)
        clusassign=model.predict(prof_data)
        meandist.append(sum(np.min(cdist(prof_data, model.cluster_centers_, 'euclidean'), axis=1))
        / prof_data.shape[0])
    
    
    # pick the fewest number of clusters that reduces the average distance
    plt.plot(k_range, meandist)
    plt.xlabel('Number of clusters')
    plt.ylabel('Average distance')
    plt.title('Selecting k with the Elbow Method')
    
    plt.show()
    

def plotScores(prof_data):

    k_range = range(2,25)#As we have 25 professors
    silhouette_scores = []
    calinski_harabaz_scores = []
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=0).fit(prof_data)
        pred_cluster = km.predict(prof_data)
        
        
        #Compute the mean Silhouette Coefficient of all samples.
        #The best value is 1 and the worst value is -1. Values near 0 indicate overlapping clusters.
        #Negative values generally indicate that a sample has been assigned to the wrong cluster, as a different cluster is more similar.
        silhouette_scores.append(silhouette_score(prof_data,pred_cluster))
        
        #print(str(calinski_harabaz_score(prof_data,pred_cluster)))
        #Compute the Calinski and Harabaz score.
        calinski_harabaz_scores.append(calinski_harabaz_score(prof_data,pred_cluster))
     
    N = len(silhouette_scores)
    x = range(N)
    width = 1/1.5
    plt.bar(x, silhouette_scores, width)
    plt.xticks(x, k_range)
    plt.ylabel('Silhouette Scores')
    plt.title('Silhouette Scores vs K')
    plt.show()
    
    
#     print(calinski_harabaz_scores)
    N = len(calinski_harabaz_scores)
    x = range(N)
    width = 1/1.5
    plt.bar(x, calinski_harabaz_scores, width)
    plt.xticks(x, k_range)
    plt.ylabel('Calinski Harabaz Scores')
    plt.title('Calinski Harabaz vs K')
    plt.show()
       
    
def plotVornoi(prof_data):
    
    pca  = PCA(2)#project to @ D data
    reduced_data = pca.fit_transform(prof_data)
    
    reduced_data = np.array(reduced_data)
    
    km = KMeans(n_clusters=num_cluster, random_state=0).fit(reduced_data)
    pred_cluster = km.predict(reduced_data)
    
    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02     # point in the mesh [x_min, x_max]x[y_min, y_max].
    
    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    
    
    # Obtain labels for each point in mesh. Use last trained model.
    Z = km.predict(np.c_[xx.ravel(), yy.ravel()])
    
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')
    
    plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
    # Plot the centroids as a white X
    centroids = km.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=169, linewidths=3,
                color='B', zorder=10)
    plt.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
              'Centroids are marked with white cross')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()
    
    
    

def predictClusterIndex(prof_data,prof_nm_lst_np):


#--------------------Normalizing the dataset--------------------#
    normalized_prof_data = preprocessing.normalize(prof_data)
    
#-------------------Standardizing the dataset-------------------#   
    standardized_prof_data = preprocessing.scale(prof_data)
   
#-----Ploting the dataset in graph with reduce dimensionality by PCA(High D => 2D)--------#   
#    reduceDimension(prof_data,prof_nm_lst_np,'actual')
    reduceDimension(normalized_prof_data,prof_nm_lst_np,'normalized')
#    reduceDimension(standardized_prof_data,prof_nm_lst_np,'standardized')

    plotElbow(normalized_prof_data)
    
    plotScores(normalized_prof_data)
    
    km = KMeans(n_clusters=num_cluster, random_state=0).fit(normalized_prof_data)
    pred_cluster = km.predict(normalized_prof_data)
    
    
    plotVornoi(normalized_prof_data)
   
    return pred_cluster
   


def func_kmeans():
    try: 
        prof_data = np.genfromtxt(hdp_csv, delimiter=',')
        
#         print("mean of the data --> "+str(np.mean(np.array(prof_data))))
#         print("standard deviation of the data --> "+str(np.std(np.array(prof_data))))
       
        
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

