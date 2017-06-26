from threading import Thread

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains
from selenium.webdriver.common import keys

import traceback
from threading import Thread
#sudo pip3 install -U nltk
#sudo pip3 install -U numpy
from nltk.stem import  WordNetLemmatizer
#sudo pip3 install gensim
from gensim import corpora, models
import os
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
#sudo pip3 install stop-words
from stop_words import get_stop_words

#sudo pip3 install pyLDAvis
#sudo pip3 install IPython
import pyLDAvis
import pyLDAvis.gensim

#sudo pip3 install wordcloud
import wordcloud

import matplotlib.pyplot as plt


import subprocess
import os

import time

import pprint

import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.model_selection import LeaveOneOut
from sklearn import preprocessing
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score,calinski_harabaz_score
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances
from sklearn.neighbors import NearestNeighbors


from scipy.spatial.distance import cdist
from scipy.spatial.distance import pdist
from scipy import sparse
from scipy.cluster.hierarchy import dendrogram,linkage


import itertools

import urllib
import requests
import pdfkit

import dblp_scrapper

from lxml import etree


paper_nm_path = "data/papernm/"
# prof_lst_file_nm = "data/faculty_list.txt"
prof_lst_file_nm = "data/faculty_list_tmp.txt"
prof_topic_file_path = "data/latenteq/"
prof_pdf_path = "data/papers/"
prof_local_pdf_path = "/home/local/ASUAD/jchakra1/Desktop/pdfs/"
prof_topic_vis_path = "data/topicvisual/"
prof_topic_dist_path = "data/topicdist/"
prof_topic_matrix_path = "data/topicmatrix/"

err_file = "data/tmp/error"
driver_name = "webdriver.chrome.driver"
#sudo apt-get install chromium-chromedriver
driver_path = "/usr/lib/chromium-browser/chromedriver"

dblp_url = "http://dblp.uni-trier.de/"


#constants
topics = 15
words = 20
time_to_wait = 30
time_to_download = 60
