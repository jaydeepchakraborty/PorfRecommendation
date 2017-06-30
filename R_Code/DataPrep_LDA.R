#setting the workspace
setwd("/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim")

######################### Variable Declaration Start #########################
img_dir = "/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim/images/"
img_extn  = ".jpeg"
######################### Variable Declaration End ###########################

######################### Loading the Data Start #########################
lda.data <- read.csv(file="lda-topic-matrix.csv", header = F)
lda.data <- lda.data*100
######################### Loading the Data End ###########################



######################### Plotting the Data Start ########################
file_path = paste(img_dir,"LDA_2D_PLOT",img_extn,sep = "")
jpeg(file = file_path)
#Standardize the data 
lda.data.stand <- as.data.frame(scale(lda.data))
lda.pca <- prcomp(lda.data.stand, scale. = TRUE)
lda.data.pca <- as.data.frame(lda.pca$x)
#Plotting with first two principle components
ggplot(lda.data.pca,aes(x=lda.data.pca[,1],y=lda.data.pca[,2]))+
  geom_point()+
  ggtitle("Scatter plot of reduced 2D LDA data")+
  xlab("PC1")+ylab("PC2")
dev.off()
######################### Plotting the Data End ########################



############## Plotting histogram of each column Start ##################
#For total 15 columns
for (ind in 1:15){
  colnm <- paste("LDA_V",ind, sep="")
  flnm <- paste(img_dir,colnm,img_extn,sep = "")
  labnm <- paste("histogram of feature",colnm, sep=" ")
  jpeg(file = flnm)
  hist(lda.data[,ind], xlab= colnm, main =labnm, col = 'pink')
  dev.off()
}
#hist(lda.data$V3)
############### Plotting histogram of each column End ###################



############## Plotting density diagram of each column Start ##################
#For total 15 columns
library(ggplot2)
pl1 <- ggplot(lda.data, aes(V5))
pl1 + geom_density(fill = "red", alpha = "0.7")
############### Plotting density diagram of each column End ###################



##################### Plotting boxplot of the Data Start ######################
flnm <- paste(img_dir,"LDA_BOX_PLOT",img_extn,sep = "")
jpeg(file = flnm)
boxplot(lda.data, horizontal = T,main="LDA_BOX_PLOT")
dev.off()
##################### Plotting boxplot of the Data End ######################


######################### Corelation Matrix Start #########################
#install.packages("corrplot")
library(corrplot)
lda.data.cor<-cor(lda.data)
flnm <- paste(img_dir,"LDA_COR_PLOT",img_extn,sep = "")
jpeg(file = flnm)
corrplot(lda.data.cor, method="circle",type="lower",title="LDA_COR_PLOT")
dev.off()
corrplot(lda.data.cor, method="color",type="lower")
corrplot(lda.data.cor, method="pie",type="lower")
corrplot(lda.data.cor, method="number",type="lower")
######################### Corelation Matrix End #########################
