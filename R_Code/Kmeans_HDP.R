#setting the workspace
setwd("/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim")
topic_matrix_ws = "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/topicmatrix/"

######################### Variable Declaration Start #########################
img_dir = "/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim/images/"
img_extn  = ".jpeg"
######################### Variable Declaration End ###########################

######################### Loading the Data Start #########################
matrix_file <- paste(topic_matrix_ws,"hdp-topic-matrix.csv",sep = "")
hdp.data <- read.csv(file=matrix_file, header = F)
hdp.data <- hdp.data*100
######################### Loading the Data End ###########################


######################### Data Preparation Start #########################
#Standardize the data 
hdp.data.stand <- as.data.frame(scale(hdp.data))
######################### Data Preparation End ###########################

############ Within groups sum of squares Calculation Start ############

# Check for the optimal number of clusters given the data
#Recall that, the basic idea behind partitioning methods, 
#such as k-means clustering, is to define clusters such that 
#the total intra-cluster variation (known as total within-cluster 
#variation or total within-cluster sum of square) is minimized:
#Check how to calculate WSS or SSW in notes
#There is no logic to find wss for cluster 1, but we are calculating it for ploting
wss <-  sum(kmeans(hdp.data.stand,centers=1)$withinss)# for cluster 1
for (i in 2:25)
  wss[i] <- sum(kmeans(hdp.data.stand,centers=i)$withinss)

file_path = paste(img_dir,"HDP_WSS_PLOT",img_extn,sep = "")
jpeg(file = file_path)
#type="l" --> line, type="p" --> point, type="b" --> both
plot(1:25, wss, type="b", 
     xlab="Number of Clusters",
     ylab="Within groups sum of squares",
     main="Assessing the Optimal Number of Clusters with the Elbow Method - HDP",
     pch=20, cex=2)
#From plot we can say 14 is the best cluster number
abline(v = 15, lty =2)
dev.off()
############ Within groups sum of squares Calculation End ############


############ Average silhouette score Calculation Start ############

#Average silhouette method computes the average silhouette of observations 
#for different values of k. The optimal number of clusters k is the one 
#that maximize the average silhouette over a range of possible values for k 
#(Kaufman and Rousseeuw [1990]).
#It will create an array where 0 is copied 15 times.check ?rep
library(cluster)
sil <- rep(0, 25)
for(i in 2:25){
  km.res <- kmeans(hdp.data.stand, centers = i, nstart = 25)
  #dist(iris.stand) it will create the Distance Matrix
  ss <- silhouette(km.res$cluster, dist(hdp.data.stand))
  #It will calculate mean of 3rd column of the output
  #ss has 3 columns :- cluster,neighbor,sil_width
  #ss then press enter, it will give following output
  #[1,]       6       13  0.625892060
  #[2,]       2        6  0.608183801 ....
  #sil[i,] contains the cluster to which i belongs
  #neighbor cluster of i
  #silhouette width of the observation
  sil[i] <- mean(ss[, 3])
}
# Plot the  average silhouette width
file_path = paste(img_dir,"HDP_SIL_PLOT",img_extn,sep = "")
jpeg(file = file_path)
plot(1:25, sil, type = "b", pch = 19, 
     frame = FALSE, xlab = "Number of clusters k", main="HDP-SILHOUETTE-SCORE")
#abline(v = which.max(sil), lty = 15)
abline(v = 15, lty = 15)
dev.off()
############ Average silhouette score Calculation End ##############


############ KMeans cluster Start ##############

#aplying kmeans for 15 clusters
hdp.data.km <- kmeans(hdp.data, 15, nstart = 20)

hdp.data.km$cluster
hdp.data.km$size

#cluster labels are added
hdp.data.clust <- data.frame(hdp.data, hdp.data.km$cluster)

#Library clusters allow us to represent (with the aid of PCA) 
#the cluster solution into 2 dimensions:
file_path = paste(img_dir,"HDP_CLUST_PLOT",img_extn,sep = "")
jpeg(file = file_path)
library(cluster)
clusplot(hdp.data.clust, hdp.data.clust$hdp.data.km.cluster, 
         main='2D representation of the HDP Cluster solution',
         color=TRUE, shade=TRUE,
         labels=0, lines=0)
dev.off()
############ KMeans cluster End ##############

############ Writting to output file Start ##############
write.csv(hdp.data.clust, file = "HDP_KCLUST_OP.csv")
############ Writting to output file End ################