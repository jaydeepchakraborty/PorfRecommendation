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


import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse




prof_lst_file_nm = "data/faculty_list.txt"
prof_topic_file_path = "data/latenteq/"
prof_pdf_path = "data/papers/"
prof_topic_vis_path = "data/topicvisual/"
prof_topic_dist_path = "data/topicdist/"
