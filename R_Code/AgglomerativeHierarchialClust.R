#This is bottom up approach: each observation starts in its own cluster 
#and pairs of clusters are merged as one moves up the hierarchy 

prof_features <- read.csv(file=file.path("/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/topicmatrix","lsa-topic-matrix.csv"))



#Normalization
z <- prof_features[,-c(1,1)]

m <- apply(z,2,mean)
s <- apply(z,2,sd)
z <- scale(z,m,s)
plot(z)

#Calculating Euclidean distance
distance <- dist(z)

#Cluster Dendogram for complete linkage
hc.complete <- hclust(distance,method = 'complete')
plot(hc.complete, labels=prof_features$Professor, hang=0.3)

#Silhouette Plot
silhouette_scores = c()
library(cluster)
for (k in 2:24){
  silhouette_scores[k-1] <- mean(silhouette(cutree(hc.complete,k),distance))
  print(mean(silhouette(cutree(hc.complete,k),distance)))
}

silhouette_scores_plot = data.frame(c(2:24),silhouette_scores)
library(ggplot2)
p <- ggplot(silhouette_scores_plot, aes(c(2:24),silhouette_scores))
p +geom_bar(stat = "identity")

#plot(silhouette(cutree(hc.complete,3),distance))

member.c <- cutree(hc.complete,5)
