#setting the workspace
ws = "/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code"
#ws = "/Users/jaydeep/jaydeep_workstation/Workplace/Kaggle/ProfSim"
setwd(ws)

######################### Variable Declaration Start #########################
img_dir = paste(ws,"/images/",sep = "")
img_extn  = ".jpeg"
######################### Variable Declaration End ###########################

######################### Loading the Data Start #########################
lda.data <- read.csv(file="lda-topic-matrix.csv", header = F)
lda.data <- lda.data*100
######################### Loading the Data End ###########################

######################### Data Preparation Start #########################
#Standardize the data 
lda.data.stand <- as.data.frame(scale(lda.data))
######################### Data Preparation End ###########################

######################### Fuzzy Clustering Start #########################
library(cluster)
lda.data.fuzzy <- fanny(lda.data.stand,10) #4 clustering
######################### Fuzzy Clustering End #########################


######################### Fuzzy Clustering Plot Start #######################
library(factoextra)
fviz_cluster(lda.data.fuzzy, frame.type = "norm", frame.level  = 0.68)
######################### Fuzzy Clustering Plot End #########################

######################### Fuzzy Silhoutte Plot Start #######################
fviz_silhouette(lda.data.fuzzy, label = TRUE)
######################### Fuzzy Silhoutte Plot End #######################

######################### Fuzzy Cluster Membership Start #######################
lda.data.fuzzy$membership
######################### Fuzzy Cluster Membership End #######################


######################### Fuzzy Corelation Plot with clusters Start #######################
library(corrplot)
corrplot(lda.data.fuzzy$membership, is.corr = FALSE)
######################### Fuzzy Corelation Plot with clusters End #######################