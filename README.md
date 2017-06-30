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

