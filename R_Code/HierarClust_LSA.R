#setting the workspace
setwd("/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim")
topic_matrix_ws = "/home/local/ASUAD/jchakra1/workspace/RecoProf/data/topicmatrix/"

######################### Variable Declaration Start #########################
img_dir = "/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim/images/"
img_extn  = ".jpeg"
######################### Variable Declaration End ###########################

######################### Loading the Data Start #########################
matrix_file <- paste(topic_matrix_ws,"lsa-topic-matrix.csv",sep = "")
lsa.data <- read.csv(file=matrix_file, header = F)
lsa.data <- lsa.data - min(lsa.data)
#lsa.data[lsa.data<0] <- 0
######################### Loading the Data End ###########################

######################### Data Preparation Start #########################
#Standardize the data 
lsa.data.stand <- as.data.frame(scale(lsa.data))
######################### Data Preparation End ###########################

############ Hierarchical cluster Start ##############
#This will calculate distance matrix, by default euclidean
lsa.data.dist = dist(lsa.data.stand, method = 'euclidean')
#Hierarchical Clustering, method can be various like single, complete, average
lsa.data.hclust = hclust(lsa.data.dist,method = "average")
############ Hierarchical cluster End ##############


############ Plotting Hierarchical cluster Start ##############
#ploting dendogram(vertical)
plot(lsa.data.hclust)
#ploting dendogram(horizontal)
plot(as.dendrogram(lsa.data.hclust), horiz = TRUE)
############ Plotting Hierarchical cluster Start ##############


############ Plotting Hierarchical cluster colored Dendogram Start ##############
# colored dendrogram
library("dendextend")
file_path = paste(img_dir,"LSA_DENDO_PLOT",img_extn,sep = "")
jpeg(file = file_path)
# using piping to get the dendogram object
dend <- as.dendrogram(lsa.data.hclust)
dend %>% color_branches(h=4) %>% plot(horiz=TRUE, main = "LSA Dendogram")
# add horizontal rectangle
dend %>% rect.dendrogram(h=4,horiz=TRUE)
# add horiz (well, vertical) line:
abline(v = 4 , lwd = 2, lty = 2, col = "blue")
dev.off()
############ Plotting Hierarchical cluster colored Dendogram End ##############


############ Plotting HeatMap Start ##############
library(gplots)
file_path = paste(img_dir,"LSA_HEATMAP_PLOT",img_extn,sep = "")
jpeg(file = file_path)
dend <- as.dendrogram(lsa.data.hclust)
hm_matrix  <- as.matrix(lsa.data)
heatmap.2(hm_matrix, Rowv = dend,srtCol=10,main="LSA HEATMAP")
dev.off()
############ Plotting HeatMap End ##############


############ Hierarchical cluster Start ##############
#getting the clusters based on height we have choosen
lsa.data.op = cutree(lsa.data.hclust,h=4)
#getting the clusters based on number of clusters we have choosen
#lsa.data.op = cutree(lsa.data.hclust,k=15)

#cluster labels are added
lsa.data.clust <- data.frame(lsa.data,lsa.data.op)
#Library clusters allow us to represent (with the aid of PCA) 
#the cluster solution into 2 dimensions:
library(cluster)
file_path = paste(img_dir,"LSA_HCLUST_PLOT",img_extn,sep = "")
jpeg(file = file_path)
clusplot(lsa.data.clust, lsa.data.clust$lsa.data.op, 
         main='2D rep of the LSA Cluster solution',
         color=TRUE, shade=TRUE,
         labels=0, lines=0)
dev.off()
############ Hierarchical cluster End ##############

############ Writting to output file Start ##############
write.csv(lsa.data.clust, file = "LSA_HCLUST_OP.csv")
############ Writting to output file End ################