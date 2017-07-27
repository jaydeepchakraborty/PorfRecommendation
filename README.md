# PorfRecommendation
Professor recommendation is a system where we are trying to find out the similarity between professors based on their research activities.

## Module1 : Data Collection

#### Tools
- Python : Selenium (http://selenium-python.readthedocs.io/)

#### Data Sources
- ASU CIDSE faculty directory: - http://cidse.engineering.asu.edu/facultyandresearch/directory/faculty/
- DBLP: - http://dblp.uni-trier.de/
- Google scholar: - https://scholar.google.com/
- IEEE, Springer, ACM, Sciencedirect, arxiv

#### Steps
- A list of professors (i.e. name) from ASU CIDSE faculty directory is collected.
- We have searched with each professor's name in DBLP and collected list of research papers for each professor.
- We have searched each research paper online and download locally.

We have collected total 5000 research papers for 60 professors.At the end of these steps we have a dataset like following 
<table>
  <tr>
    <td>prof1</td>
    <td>101 research papers</td>
  </tr>
  <tr>
    <td>prof2</td>
    <td>67 research papers</td>
  </tr>
  <tr>
    <td>....</td>
    <td>....</td>
  </tr>
  <tr>
    <td>prof60</td>
    <td>159 research papers</td>
  </tr>
</table>

## Module2 : Data Preparation
- We have converted each research paper into text file and combined them for each professor.

At the end of this step we have a dataset like following 
<table>
  <tr>
    <td>prof1</td>
    <td>1 text file [concatenation or combination of 101 research papers]</td>
  </tr>
  <tr>
    <td>prof2</td>
    <td>1 text file [concatenation or combination of 67 research papers]</td>
  </tr>
  <tr>
    <td>....</td>
    <td>....</td>
  </tr>
  <tr>
    <td>prof60</td>
    <td>1 text file [concatenation or combination of 159 research papers]</td>
  </tr>
</table>

## Module3 : Topic Modelling
Topic modelling is a statistical modeling which helps to discover latent or hidden topics in a text or bag of words. In topic modelling, we have used the following algorithms.

1. Latent Semantic Analysis (LSA)
2. Latent  Dirichlet  allocation (LDA)
3. Hierarchical  Dirichlet  process (HDP) 

#### Tools
- Python : gensim (https://radimrehurek.com/gensim/)
- Python : scikit-learn (http://scikit-learn.org/stable/)
- Python : nltk (http://www.nltk.org/index.html#)

#### Steps
We have followed the following steps for all the three algorithms.
- We have read the text file for each professor
- Tokenize the entire data by words.
- Remove stop words from the tokenized data.
  1. common english stop words. (stop-words is available on PyPi; stop-words 2015.2.23.1)
  2. non english words.
  3. digits.
  4. custom stop words. To create the custom stop words, we have used wordcloud (wordcloud 1.3.1) and pyLDAvis (pyLDAvis 2.1.1). We manually checked all the words which are unnecessary and added those to custom stop word list.
- Stemming the tokenized data. It is a process to convert the words to their roots. (http://www.nltk.org/api/nltk.stem.html)
- Convert tokenized documents into a id <-> term dictionary.
- Convert tokenized documents into document - term matrix
- Apply all three algorithms to find out latent topics (Here, we have considered 15 topics)
- In the last step we have find out the probability of topic distribution among the documents.

At the end of these steps we have a dataset like following for each three algorithms.
<table>
  <tr>
    <td></td>
    <td>Topic1</td>
    <td>Topic2</td>
    <td>....</td>
    <td>Topic15</td>
  </tr>
  <tr>
    <td>Prof1</td>
    <td>39%</td>
    <td>15%</td>
    <td>....</td>
    <td>18%</td>
  </tr>
  <tr>
    <td>Prof2</td>
    <td>70%</td>
    <td>2%</td>
    <td>....</td>
    <td>9%</td>
  </tr>
  <tr>
    <td>....</td>
    <td>....</td>
    <td>....</td>
    <td>....</td>
    <td>....</td>
  </tr>
  <td>Prof60</td>
    <td>10%</td>
    <td>12%</td>
    <td>....</td>
    <td>67%</td>
</table>

## Module4 : Clustering
Clustering is grouping of data based on their similarities. We have used the following clustering method.
1. K-means clustering
2. Hierarchical clustering (Agglomerative)

#### Tools
- R (https://cran.r-project.org/)

#### Steps
1. *Data Analysis*

We have plotted the data in 2d space by using PCA (Principal Component Analysis).
<table>
  <tr>
    <td><img width="250" height="250" alt="LSA_2D_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_2D_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_2D_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_2D_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_2D_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_2D_PLOT.jpeg"></td>
  </tr>
</table>

We have plotted the histogram of each attribute or column for each algorithm to check the data distribution.</br>
- LSA Data Histogram
<table>
  <tr>
    <td><img width="150" height="200" alt="LSA_V1" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V1.jpeg"></td>
    <td><img width="150" height="200" alt="LSA_V2" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V2.jpeg"></td>
    <td><img width="150" height="200" alt="LSA_V3" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V3.jpeg"></td>
     <td><img width="150" height="200" alt="LSA_V4" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V4.jpeg"></td>
    <td><img width="150" height="200" alt="LSA_V5" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V5.jpeg"></td>
  </tr>
  <tr>
    <td><img width="150" height="200" alt="LSA_V6" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V6.jpeg"></td>
    <td><img width="150" height="200" alt="LSA_V7" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V7.jpeg"></td>
    <td><img width="150" height="200" alt="LSA_V8" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V8.jpeg"></td>
     <td><img width="150" height="200" alt="LSA_V9" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V9.jpeg"></td>
    <td><img width="150" height="200" alt="LSA_V10" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V10.jpeg"></td>
  </tr>
  <tr>
    <td><img width="150" height="200" alt="LSA_V11" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V11.jpeg"></td>
    <td><img width="150" height="200" alt="LSA_V12" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V12.jpeg"></td>
    <td><img width="150" height="200" alt="LSA_V13" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V13.jpeg"></td>
     <td><img width="150" height="200" alt="LSA_V14" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V14.jpeg"></td>
    <td><img width="150" height="200" alt="LSA_V15" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_V15.jpeg"></td>
  </tr>
</table>

- LDA Data Histogram

<table>
  <tr>
    <td><img width="150" height="200" alt="LDA_V1" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V1.jpeg"></td>
    <td><img width="150" height="200" alt="LDA_V2" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V2.jpeg"></td>
    <td><img width="150" height="200" alt="LDA_V3" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V3.jpeg"></td>
     <td><img width="150" height="200" alt="LDA_V4" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V4.jpeg"></td>
    <td><img width="150" height="200" alt="LDA_V5" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V5.jpeg"></td>
  </tr>
  <tr>
    <td><img width="150" height="200" alt="LDA_V6" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V6.jpeg"></td>
    <td><img width="150" height="200" alt="LDA_V7" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V7.jpeg"></td>
    <td><img width="150" height="200" alt="LDA_V8" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V8.jpeg"></td>
     <td><img width="150" height="200" alt="LDA_V9" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V9.jpeg"></td>
    <td><img width="150" height="200" alt="LDA_V10" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V10.jpeg"></td>
  </tr>
  <tr>
    <td><img width="150" height="200" alt="LDA_V11" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V11.jpeg"></td>
    <td><img width="150" height="200" alt="LDA_V12" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V12.jpeg"></td>
    <td><img width="150" height="200" alt="LDA_V13" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V13.jpeg"></td>
     <td><img width="150" height="200" alt="LDA_V14" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V14.jpeg"></td>
    <td><img width="150" height="200" alt="LDA_V15" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_V15.jpeg"></td>
  </tr>
</table>

- HDP Data Histogram

<table>
  <tr>
    <td><img width="150" height="200" alt="HDP_V1" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V1.jpeg"></td>
    <td><img width="150" height="200" alt="HDP_V2" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V2.jpeg"></td>
    <td><img width="150" height="200" alt="HDP_V3" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V3.jpeg"></td>
     <td><img width="150" height="200" alt="HDP_V4" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V4.jpeg"></td>
    <td><img width="150" height="200" alt="HDP_V5" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V5.jpeg"></td>
  </tr>
  <tr>
    <td><img width="150" height="200" alt="HDP_V6" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V6.jpeg"></td>
    <td><img width="150" height="200" alt="HDP_V7" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V7.jpeg"></td>
    <td><img width="150" height="200" alt="HDP_V8" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V8.jpeg"></td>
     <td><img width="150" height="200" alt="HDP_V9" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V9.jpeg"></td>
    <td><img width="150" height="200" alt="HDP_V10" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V10.jpeg"></td>
  </tr>
  <tr>
    <td><img width="150" height="200" alt="HDP_V11" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V11.jpeg"></td>
    <td><img width="150" height="200" alt="HDP_V12" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V12.jpeg"></td>
    <td><img width="150" height="200" alt="HDP_V13" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V13.jpeg"></td>
     <td><img width="150" height="200" alt="HDP_V14" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V14.jpeg"></td>
    <td><img width="150" height="200" alt="HDP_V15" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_V15.jpeg"></td>
  </tr>
</table>

We have plotted the boxplot for each algorithm
<table>
  <tr>
    <td><img width="250" height="250" alt="LSA_BOX_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_BOX_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_BOX_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_BOX_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_BOX_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_BOX_PLOT.jpeg"></td>
  </tr>
</table>

We have plotted the corelation matrix for each algorithm
<table>
  <tr>
    <td><img width="250" height="250" alt="LSA_COR_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_COR_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_COR_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_COR_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_COR_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_COR_PLOT.jpeg"></td>
  </tr>
</table>

2. *K-means clustering*

  In K-means algorithm, to find the optimal value of K, we have used the following methods
  1. Elbow method
  
  Here we have plotted within-cluster sum of square (WSS) and try to find out minimum value of WSS keeping the cluster value(K) lowest.
  <table>
  <tr>
    <td><img width="250" height="250" alt="LSA_WSS_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_WSS_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_WSS_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_WSS_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_WSS_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_WSS_PLOT.jpeg"></td>
  </tr>
</table>

  2. Maximum average silhouette score
  
  Here we have plotted average silhouette score (Kaufman and Rousseeuw [1990]) for a range of cluster. The optimal number of clusters k is the one that maximize the average silhouette over a range of possible values for k 
  
  <table>
  <tr>
    <td><img width="250" height="250" alt="LSA_SIL_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_SIL_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_SIL_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_SIL_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_SIL_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_SIL_PLOT.jpeg"></td>
  </tr>
</table>

The next images are cluster plots for each algorithm.

<table>
  <tr>
    <td><img width="250" height="250" alt="LSA_CLUST_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_CLUST_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_CLUST_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_CLUST_PLOT.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_CLUST_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_CLUST_PLOT.jpeg"></td>
  </tr>
</table>


3. *Hierarchical clustering (Agglomerative)*

We have plotted dendogram for each algorithm

<table>
<tr>
    <td>LSA Dendogram with single linkage</td>
    <td>LSA Dendogram with complete linkage</td>
    <td>LSA Dendogram with average linkage</td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="LSA_DENDO_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_DENDO_PLOT_single.jpeg"></td>
    <td><img width="250" height="250" alt="LSA_DENDO_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_DENDO_PLOT_complete.jpeg"></td>
    <td><img width="250" height="250" alt="LSA_DENDOT_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_DENDO_PLOT_average.jpeg"></td>
  </tr>
</table>


<table>
<tr>
    <td>LDA Dendogram with single linkage</td>
    <td>LDA Dendogram with complete linkage</td>
    <td>LDA Dendogram with average linkage</td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="LDA_DENDO_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_DENDO_PLOT_single.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_DENDO_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_DENDO_PLOT_complete.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_DENDOT_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_DENDO_PLOT_average.jpeg"></td>
  </tr>
</table>

<table>
<tr>
    <td>HDP Dendogram with single linkage</td>
    <td>HDP Dendogram with complete linkage</td>
    <td>HDP Dendogram with average linkage</td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="HDP_DENDO_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_DENDO_PLOT_single.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_DENDO_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_DENDO_PLOT_complete.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_DENDOT_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_DENDO_PLOT_average.jpeg"></td>
  </tr>
</table>

We have plotted heatmap for each algorithm

<table>
<tr>
    <td>LSA Heatmap with single linkage</td>
    <td>LSA Heatmap with complete linkage</td>
    <td>LSA Heatmap with average linkage</td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="LSA_HEATMAP_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_HEATMAP_PLOT_single.jpeg"></td>
    <td><img width="250" height="250" alt="LSA_HEATMAP_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_HEATMAP_PLOT_complete.jpeg"></td>
    <td><img width="250" height="250" alt="LSA_HEATMAP_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_HEATMAP_PLOT_average.jpeg"></td>
  </tr>
</table>

<table>
<tr>
    <td>LDA Heatmap with single linkage</td>
    <td>LDA Heatmap with complete linkage</td>
    <td>LDA Heatmap with average linkage</td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="LDA_HEATMAP_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_HEATMAP_PLOT_single.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_HEATMAP_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_HEATMAP_PLOT_complete.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_HEATMAP_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_HEATMAP_PLOT_average.jpeg"></td>
  </tr>
</table>

<table>
<tr>
    <td>HDP Heatmap with single linkage</td>
    <td>HDP Heatmap with complete linkage</td>
    <td>HDP Heatmap with average linkage</td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="HDP_HEATMAP_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_HEATMAP_PLOT_single.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_HEATMAP_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_HEATMAP_PLOT_complete.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_HEATMAP_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_HEATMAP_PLOT_average.jpeg"></td>
  </tr>
</table>

The next images are cluster plots for each algorithm.

<table>
<tr>
    <td>LSA clustering with single linkage</td>
    <td>LSA clustering with complete linkage</td>
    <td>LSA clustering with average linkage</td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="LSA_HCLUST_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_HCLUST_PLOT_single.jpeg"></td>
    <td><img width="250" height="250" alt="LSA_HCLUST_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_HCLUST_PLOT_complete.jpeg"></td>
    <td><img width="250" height="250" alt="LSA_HCLUST_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LSA_HCLUST_PLOT_average.jpeg"></td>
  </tr>
</table>

<table>
<tr>
    <td>LDA clustering with single linkage</td>
    <td>LDA clustering with complete linkage</td>
    <td>LDA clustering with average linkage</td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="LDA_HCLUST_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_HCLUST_PLOT_single.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_HCLUST_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_HCLUST_PLOT_complete.jpeg"></td>
    <td><img width="250" height="250" alt="LDA_HCLUST_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/LDA_HCLUST_PLOT_average.jpeg"></td>
  </tr>
</table>

<table>
<tr>
    <td>HDP clustering with single linkage</td>
    <td>HDP clustering with complete linkage</td>
    <td>HDP clustering with average linkage</td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="HDP_HCLUST_PLOT"    src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_HCLUST_PLOT_single.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_HCLUST_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_HCLUST_PLOT_complete.jpeg"></td>
    <td><img width="250" height="250" alt="HDP_HCLUST_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/HDP_HCLUST_PLOT_average.jpeg"></td>
  </tr>
</table>


## Module5 : Survey and Creation of Gold Copy

To evaluate our system, we took help from some experts. We have setup a survey form where experts are asked two professors or scholars are similar or not. All of the experts filled up the survey based on their knowledge. As our experiment is Binary classification so in order to measure the performance we have created a gold standard copy. We have considered most votes for a particular professor or scholar pair i.e if 50% or more than 50% said yes then we considered that scholar or professor pair is similar in gold standard copy otherwise dissimilar.

We have used Krippendorff's alpha reliability to measure the inter reliability among experts. (https://rdrr.io/cran/irr/man/kripp.alpha.html). Ideally Krippendorff's alpha's value should be => 80%. But unfortunetly we got 34%. In our case it does not that matter because we are counting max vote for a professor pair. But if we do any regression insted of classification then this Krippendorff's alpha matters most. 


## Module6 : Calculate Accuracy
It is a binary classification problem, we have used following measures. This two links are very informative about accuracy calculation(1) http://scikit-learn.org/stable/modules/model_evaluation.html# and 2) http://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation)

For Kmeans algorithm
<table>
<tr>
    <td></td>
    <td>F1 score</td>
    <td>Precision score</td>
    <td>Recall score</td>
    <td>Accuracy score</td>
  </tr>
  <tr>
    <td>LSA</td>
    <td>0.0972404730618</td>
    <td>0.0547337278107</td>
    <td>0.435294117647</td>
    <td>0.61186440678</td>
  </tr>
  <tr>
    <td>LDA</td>
    <td>0.176470588235</td>
    <td>0.128342245989</td>
    <td>0.282352941176</td>
    <td>0.873446327684</td>
  </tr>
  <tr>
    <td>HDP</td>
    <td>0.127272727273</td>
    <td>0.103703703704</td>
    <td>0.164705882353</td>
    <td>0.891525423729</td>
  </tr>
</table>


For Hierarchical Clustering algorithm
<table>
<tr>
    <td></td>
    <td>F1 score</td>
    <td>Precision score</td>
    <td>Recall score</td>
    <td>Accuracy score</td>
  </tr>
  <tr>
    <td>LSA</td>
    <td>0.095717884131</td>
    <td>0.0535966149506</td>
    <td>0.447058823529</td>
    <td>0.594350282486</td>
  </tr>
  <tr>
    <td>LDA</td>
    <td>0.180904522613</td>
    <td>0.157894736842</td>
    <td>0.211764705882</td>
    <td>0.90790960452</td>
  </tr>
  <tr>
    <td>HDP</td>
    <td>0.133828996283</td>
    <td>0.0978260869565</td>
    <td>0.211764705882</td>
    <td>0.868361581921</td>
  </tr>
</table>

For Kmeans algorithm
<table>
<tr>
    <td></td>
    <td>TN</td>
    <td>FP</td>
    <td>FN</td>
    <td>TP</td>
  </tr>
  <tr>
    <td>LSA</td>
    <td>1046</td>
    <td>639</td>
    <td>48</td>
    <td>37</td>
  </tr>
  <tr>
    <td>LDA</td>
    <td>1522</td>
    <td>163</td>
    <td>61</td>
    <td>24</td>
  </tr>
  <tr>
    <td>HDP</td>
    <td>1564</td>
    <td>121</td>
    <td>71</td>
    <td>14</td>
  </tr>
</table>

For Hierarchical clustering algorithm
<table>
<tr>
    <td></td>
    <td>TN</td>
    <td>FP</td>
    <td>FN</td>
    <td>TP</td>
  </tr>
  <tr>
    <td>LSA</td>
    <td>1014</td>
    <td>671</td>
    <td>47</td>
    <td>38</td>
  </tr>
  <tr>
    <td>LDA</td>
    <td>1589</td>
    <td>96</td>
    <td>67</td>
    <td>18</td>
  </tr>
  <tr>
    <td>HDP</td>
    <td>1519</td>
    <td>166</td>
    <td>67</td>
    <td>18</td>
  </tr>
</table>

For Kmeans algorithm
<table>
<tr>
    <td></td>
    <td>Cohen Kappa score</td>
    <td>V measure score</td>
    <td>Adjusted Rand Index</td>
  </tr>
  <tr>
    <td>LSA</td>
    <td>0.000699402667944</td>
    <td>0.00459466788655</td>
    <td>0.0130351852603</td>
  </tr>
  <tr>
    <td>LDA</td>
    <td>0.118247525853</td>
    <td>0.0232230523619</td>
    <td>0.100703683798</td>
  </tr>
  <tr>
    <td>HDP</td>
    <td>0.009473945673</td>
    <td>0.0636292624162</td>
    <td>0.0726156365125</td>
  </tr>
</table>

For Hierarchical clustering algorithm
<table>
<tr>
    <td></td>
    <td>Cohen Kappa score</td>
    <td>V measure score</td>
    <td>Adjusted Rand Index</td>
  </tr>
  <tr>
    <td>LSA</td>
    <td>0.000518929665546</td>
    <td>0.00329845464859</td>
    <td>0.0108884305561</td>
  </tr>
  <tr>
    <td>LDA</td>
    <td>0.133213159081</td>
    <td>0.0281293548164</td>
    <td>0.119429450267</td>
  </tr>
  <tr>
    <td>HDP</td>
    <td>0.00963934402175</td>
    <td>0.0616611244637</td>
    <td>0.0729234573452</td>
  </tr>
</table>

ROC Curve for Kmeans and Hierarchical clustering algorithm

<table>
<tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="LSA_2D_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/ROC_Kmeans.png"></td>
    <td><img width="250" height="250" alt="LSA_2D_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/ROC_HClust.png"></td>
  </tr>
  </table
  
 Precision - Recall Curve for Kmeans and Hierarchical clustering algorithm

<table>
<tr>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td><img width="250" height="250" alt="LSA_2D_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/Precision_Recall_Kmeans.png"></td>
    <td><img width="250" height="250" alt="LSA_2D_PLOT" src="https://github.com/jaydeepchakraborty/PorfRecommendation/blob/dev/data/tmp/images/Precision_Recall_HClust.png"></td>
  </tr>
  </table

