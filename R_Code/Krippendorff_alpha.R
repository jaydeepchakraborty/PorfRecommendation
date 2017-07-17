
setwd("/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code/")

library(irr)
krip.data <- read.csv(file="gold_copy.csv", header = T)
krip.matrix <- t(as.matrix(krip.data))
kripp.alpha(krip.matrix,"nominal")


r1 <- krip.data[,1]
r2 <- krip.data[,2]
r3 <- krip.data[,3]


plot(r1,type = "p",col = "red", xlab = "datapoint", ylab = "rate", 
     main = "Rater Chart")

lines(r2, type = "p", col = "blue")
lines(r3, type = "p", col = "green")