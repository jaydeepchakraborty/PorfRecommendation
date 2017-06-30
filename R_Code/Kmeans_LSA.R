#setting the workspace
setwd("/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim")

######################### Variable Declaration Start #########################
img_dir = "/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim/images/"
img_extn  = ".jpeg"
######################### Variable Declaration End ###########################

######################### Loading the Data Start #########################
lsa.data <- read.csv(file="lsa-topic-matrix.csv", header = F)
lsa.data <- lsa.data - min(lsa.data)
######################### Loading the Data End ###########################

######################### Data Preparation Start #########################
#Standardize the data 
lsa.data.stand <- as.data.frame(scale(lsa.data))
######################### Data Preparation End ###########################

############ Within groups sum of squares Calculation Start ############

# Check for the optimal number of clusters given the data
#Recall that, the basic idea behind partitioning methods, 
#such as k-means clustering, is to define clusters such that 
#the total intra-cluster variation (known as total within-cluster 
#variation or total within-cluster sum of square) is minimized:
#Check how to calculate WSS or SSW in notes
#There is no logic to find wss for cluster 1, but we are calculating it for ploting
wss <-  sum(kmeans(lsa.data.stand,centers=1)$withinss)# for cluster 1
for (i in 2:25)
  wss[i] <- sum(kmeans(lsa.data.stand,centers=i)$withinss)

file_path = paste(img_dir,"LSA_WSS_PLOT",img_extn,sep = "")
jpeg(file = file_path)
#type="l" --> line, type="p" --> point, type="b" --> both
plot(1:25, wss, type="b", 
     xlab="Number of Clusters",
     ylab="Within groups sum of squares",
     main="Assessing the Optimal Number of Clusters with the Elbow Method - LSA",
     pch=20, cex=2)
#From plot we can say 14 is the best cluster number
abline(v = 16, lty =2)
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
  km.res <- kmeans(lsa.data.stand, centers = i, nstart = 25)
  #dist(iris.stand) it will create the Distance Matrix
  ss <- silhouette(km.res$cluster, dist(lsa.data.stand))
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
file_path = paste(img_dir,"LSA_SIL_PLOT",img_extn,sep = "")
jpeg(file = file_path)
plot(1:25, sil, type = "b", pch = 19, 
     frame = FALSE, xlab = "Number of clusters k", main="LSA-SILHOUETTE-SCORE")
abline(v = which.max(sil), lty = 16)
dev.off()
############ Average silhouette score Calculation End ##############


############ KMeans cluster Start ##############

#aplying kmeans for 14 clusters
lsa.data.km <- kmeans(lsa.data.stand, 16, nstart = 20)

lsa.data.km$cluster
lsa.data.km$size

#cluster labels are added
lsa.data.clust <- data.frame(lsa.data, lsa.data.km$cluster)

#Library clusters allow us to represent (with the aid of PCA) 
#the cluster solution into 2 dimensions:
library(cluster)
file_path = paste(img_dir,"LSA_CLUST_PLOT",img_extn,sep = "")
jpeg(file = file_path)
clusplot(lsa.data.clust, lsa.data.clust$lsa.data.km.cluster, 
         main='2D representation of the LSA Cluster solution',
         color=TRUE, shade=TRUE,
         labels=0, lines=0)
dev.off()
############ KMeans cluster End ##############

############ Writting to output file Start ##############
write.csv(lsa.data.clust, file = "LSA_KCLUST_OP.csv")
############ Writting to output file End ################