# PorfRecommendation
Professor recommendation is a system where we are trying to find out the similarity between professors based on their research activities.

## Module1 : Data Collection

#### Tools
- Python
- Selenium

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
Topic modelling is a statisticalmodeling  which  helps  to  discover  latent  or  hidden  topics in  a  text  or  bag  of  words. In topic modelling, we have used the following algorithms.

1. Latent Semantic Analysis (LSA)
2. Latent  Dirichlet  allocation (LDA)
3. Hierarchical  Dirichlet  process (HDP) 
