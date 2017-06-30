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
