setwd("/home/local/ASUAD/jchakra1/workspace/RecoProf/R_Code")

require(XML)
url <- ('http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7889510')
download.file(url, 'introductionToR.pdf', mode="wb")