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



######################### Plotting the Data Start ########################
file_path = paste(img_dir,"HDP_2D_PLOT",img_extn,sep = "")
jpeg(file = file_path)
#Standardize the data 
library(ggplot2)
hdp.data.stand <- as.data.frame(scale(hdp.data))
hdp.pca <- prcomp(hdp.data.stand, scale. = TRUE)
hdp.data.pca <- as.data.frame(hdp.pca$x)
#Plotting with first two principle components
ggplot(hdp.data.pca,aes(x=hdp.data.pca[,1],y=hdp.data.pca[,2]))+
  geom_point()+
  ggtitle("Scatter plot of reduced 2D HDP data")+
  xlab("PC1")+ylab("PC2")
dev.off()
######################### Plotting the Data End ########################



############## Plotting histogram of each column Start ##################
#For total 15 columns
for (ind in 1:15){
  colnm <- paste("HDP_V",ind, sep="")
  flnm <- paste(img_dir,colnm,img_extn,sep = "")
  labnm <- paste("histogram of feature",colnm, sep=" ")
  jpeg(file = flnm)
  hist(hdp.data[,ind], xlab= colnm, main =labnm, col = 'pink')
  dev.off()
}
#hist(hdp.data$V3)
############### Plotting histogram of each column End ###################



############## Plotting density diagram of each column Start ##################
#For total 15 columns
library(ggplot2)
pl1 <- ggplot(hdp.data, aes(V5))
pl1 + geom_density(fill = "red", alpha = "0.7")
############### Plotting density diagram of each column End ###################



##################### Plotting boxplot of the Data Start ######################
flnm <- paste(img_dir,"HDP_BOX_PLOT",img_extn,sep = "")
jpeg(file = flnm)
boxplot(hdp.data, horizontal = T,main="HDP_BOX_PLOT")
dev.off()
##################### Plotting boxplot of the Data End ######################


######################### Corelation Matrix Start #########################
#install.packages("corrplot")
library(corrplot)
hdp.data.cor<-cor(hdp.data)
flnm <- paste(img_dir,"HDP_COR_PLOT",img_extn,sep = "")
jpeg(file = flnm)
corrplot(hdp.data.cor, method="circle",type="lower",title="HDP_COR_PLOT")
dev.off()
corrplot(hdp.data.cor, method="color",type="lower")
corrplot(hdp.data.cor, method="pie",type="lower")
corrplot(hdp.data.cor, method="number",type="lower")
######################### Corelation Matrix End #########################
