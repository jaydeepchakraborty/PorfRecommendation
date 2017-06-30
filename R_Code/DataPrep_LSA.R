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



######################### Plotting the Data Start ########################
flnm = paste(img_dir,"LSA_2D_PLOT",img_extn,sep = "")
jpeg(file = flnm)
#Standardize the data
lsa.data.stand <- as.data.frame(scale(lsa.data))
lsa.pca <- prcomp(lsa.data.stand, scale. = TRUE)
lsa.data.pca <- as.data.frame(lsa.pca$x)
#Plotting with first two principle components
ggplot(lsa.data.pca,aes(x=lsa.data.pca[,1],y=lsa.data.pca[,2]))+
  geom_point()+
  ggtitle("Scatter plot of reduced 2D LSA data")+
  xlab("PC1")+ylab("PC2")
dev.off()
######################### Plotting the Data End ########################



############## Plotting histogram of each column Start ##################
#For total 15 columns
for (ind in 1:15){
  colnm <- paste("LSA_V",ind, sep="")
  flnm <- paste(img_dir,colnm,img_extn,sep = "")
  labnm <- paste("histogram of feature",colnm, sep=" ")
  jpeg(file = flnm)
  hist(lsa.data[,ind], xlab= colnm, main =labnm, col = 'pink')
  dev.off()
}
#hist(lsa.data$V1)
############### Plotting histogram of each column End ###################



############## Plotting density diagram of each column Start ##################
#For total 15 columns
library(ggplot2)
pl1 <- ggplot(lsa.data, aes(V5))
pl1 + geom_density(fill = "red", alpha = "0.7")
############### Plotting density diagram of each column End ###################



##################### Plotting boxplot of the Data Start ######################
flnm <- paste(img_dir,"LSA_BOX_PLOT",img_extn,sep = "")
jpeg(file = flnm)
boxplot(lsa.data, horizontal = T,main="LSA_BOX_PLOT")
dev.off()
##################### Plotting boxplot of the Data End ######################


######################### Corelation Matrix Start #########################
#install.packages("corrplot")
library(corrplot)
lsa.data.cor<-cor(lsa.data)
flnm <- paste(img_dir,"LSA_COR_PLOT",img_extn,sep = "")
jpeg(file = flnm)
corrplot(lsa.data.cor, method="circle",type="lower",title="LSA_COR_PLOT")
dev.off()
corrplot(lsa.data.cor, method="color",type="lower")
corrplot(lsa.data.cor, method="pie",type="lower")
corrplot(lsa.data.cor, method="number",type="lower")
######################### Corelation Matrix End #########################
