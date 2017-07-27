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

############ Hierarchical cluster Start ##############
#This will calculate distance matrix, by default euclidean
hdp.data.dist = dist(hdp.data.stand, method = 'euclidean')
#Hierarchical Clustering, method can be various like single, complete, average
hdp.data.hclust = hclust(hdp.data.dist,method = "complete")
############ Hierarchical cluster End ##############


############ Plotting Hierarchical cluster Start ##############
#ploting dendogram(vertical)
plot(hdp.data.hclust)
#ploting dendogram(horizontal)
plot(as.dendrogram(hdp.data.hclust), horiz = TRUE)
############ Plotting Hierarchical cluster Start ##############

############ Plotting Hierarchical cluster colored Dendogram Start ##############
# colored dendrogram
library("dendextend")
file_path = paste(img_dir,"HDP_DENDO_PLOT",img_extn,sep = "")
jpeg(file = file_path)
# using piping to get the dendogram object
dend <- as.dendrogram(hdp.data.hclust)
dend %>% color_branches(h=5) %>% plot(horiz=TRUE, main = "HDP Dendogram")
# add horizontal rectangle
dend %>% rect.dendrogram(h=5,horiz=TRUE)
# add horiz (well, vertical) line:
abline(v = 5 , lwd = 2, lty = 2, col = "blue")
dev.off()
############ Plotting Hierarchical cluster colored Dendogram End ##############


############ Plotting HeatMap Start ##############
#ploting heatMap
library(gplots)
file_path = paste(img_dir,"HDP_HEATMAP_PLOT",img_extn,sep = "")
jpeg(file = file_path)
dend <- as.dendrogram(hdp.data.hclust)
hm_matrix  <- as.matrix(hdp.data)
heatmap.2(hm_matrix, Rowv = dend,srtCol=10,main="HDP HEATMAP")
dev.off()
############ Plotting HeatMap End ##############


#getting the clusters based on height we have choosen
hdp.data.op = cutree(hdp.data.hclust,h=5)
#getting the clusters based on number of clusters we have choosen
#hdp.data.op = cutree(hdp.data.hclust,k=15)

#cluster labels are added
hdp.data.clust <- data.frame(hdp.data,hdp.data.op)
#Library clusters allow us to represent (with the aid of PCA) 
#the cluster solution into 2 dimensions:
library(cluster)
file_path = paste(img_dir,"HDP_HCLUST_PLOT",img_extn,sep = "")
jpeg(file = file_path)
clusplot(hdp.data.clust, hdp.data.clust$hdp.data.op, 
         main='2D rep of the HDP Cluster solution',
         color=TRUE, shade=TRUE,
         labels=0, lines=0)
dev.off()

############ Writting to output file Start ##############
write.csv(hdp.data.clust, file = "HDP_HCLUST_OP.csv")
############ Writting to output file End ################