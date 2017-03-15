'''
This file is for topic modelling for each professor all together
'''


from recoprofconst import *
from custom_stopword import *


tokenizer = RegexpTokenizer(r'\w+')
p_stemmer = PorterStemmer()
en_stop = get_stop_words('en') + custom_stop_lst


def writeProbEq(proflst):
    #list all the documents(only texts) for a professor  
    prof_doc_set = []
    for prof in proflst:
        for file_nm in os.listdir(prof_pdf_path+prof):
            if file_nm.endswith(".pdf.txt"):
                with open(prof_pdf_path+prof+"/"+file_nm, 'r',  encoding='latin-1') as prof_file:
                    prof_doc_set.append(prof_file.read().replace('\n', ' '))
    
    
    #list for tokenized documents in loop
    prof_texts = []
    for prof_doc in prof_doc_set:
        
        #clean and tokenize document
        raw_data = prof_doc.lower()
        tokens = tokenizer.tokenize(raw_data)
    
        #remove stop words from tokens
        
        stopped_tokens = [i for i in tokens if not i in en_stop]
        
        #stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        
        #add tokens to list
        prof_texts.append(stemmed_tokens)
    
    #turn our tokenized documents into a id <-> term dictionary    
    dictionary = corpora.Dictionary(prof_texts)    
    #convert tokenized documents into document - term matrix
    corpus = [dictionary.doc2bow(text) for text in prof_texts]
    
    
    #Creating folder for saving visual files
    prof_topic_vis_file_nm = prof_topic_vis_file_path+"total/"
    os.makedirs(os.path.dirname(prof_topic_vis_file_nm),exist_ok=True)
    
    #----------------------------------------------------------------------------------------------------------------- 
    try:
        prof_lsa_topic_file_nm = prof_topic_file_path+"total/"+"total-lsa"+'.txt'
        os.makedirs(os.path.dirname(prof_lsa_topic_file_nm),exist_ok=True)
        lsa_latent_topic_file = open(prof_lsa_topic_file_nm, "w", encoding='latin1')
            
        lsa_model = models.lsimodel.LsiModel(corpus=corpus, id2word=dictionary, num_topics=50)
        for model in lsa_model.show_topics(formatted=True,num_topics=50,num_words=30):
            lsa_latent_topic_file.write(str(model))
            lsa_latent_topic_file.write("\n")

#NOT WORKING AS PYLDAVIS DOES NOT SUPPORT LSA         
#         lsa_data = pyLDAvis.gensim.prepare(lsa_model,corpus,dictionary)
#         pyLDAvis.display(lsa_data)
#         pyLDAvis.save_html(lsa_data, prof_topic_vis_file_nm+"lsa.html")

        lsa_latent_topic_file.close()
        #Creating Word Cloud
        for topic in open(prof_lsa_topic_file_nm,'rt', encoding='latin1'):
            topic_lsa_dict = {}
            for tmptopic in topic.split(",")[1].strip()[1:-1].split("+"):
                wight = tmptopic.split("*\"")[0].strip()
                term  = tmptopic.split("*\"")[1].strip()[:-1]
                topic_lsa_dict[term] = float(wight)*1000
              
            topic_cloud = wordcloud.WordCloud().generate_from_frequencies(topic_lsa_dict, max_font_size=None)
            plt.imshow(topic_cloud,interpolation='bilinear')
            plt.axis("off")
            plt.draw()
            plt.savefig(prof_topic_vis_file_nm+"lsa_topic"+topic.split(",")[0].strip()[1:]+".png",dpi=1000)
           
    except:
        traceback.print_exc()
        pass
    #-----------------------------------------------------------------------------------------------------------------   
    try:
        prof_lda_topic_file_nm = prof_topic_file_path+"total/"+"total-lda"+'.txt'
        os.makedirs(os.path.dirname(prof_lda_topic_file_nm),exist_ok=True)
        lda_latent_topic_file = open(prof_lda_topic_file_nm, "w", encoding='latin1')
         
        lda_model = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=50, 
                                           update_every=1, chunksize=10000, passes=20)
        for model in lda_model.show_topics(num_topics=50,num_words=30,formatted=True):
            lda_latent_topic_file.write(str(model))
            lda_latent_topic_file.write("\n")
     
         
        lda_data = pyLDAvis.gensim.prepare(lda_model,corpus,dictionary)
        pyLDAvis.display(lda_data)
        pyLDAvis.save_html(lda_data, prof_topic_vis_file_nm+"lda.html")
    except:
        traceback.print_exc()
        pass
    
    #-----------------------------------------------------------------------------------------------------------------   
    try:
        prof_hdp_topic_file_nm = prof_topic_file_path+"total/"+"total-hdp"+'.txt'
        os.makedirs(os.path.dirname(prof_hdp_topic_file_nm),exist_ok=True)
        hdp_latent_topic_file = open(prof_hdp_topic_file_nm, "w", encoding='latin1')
         
        hdp_model = models.hdpmodel.HdpModel(corpus, id2word=dictionary)
        for model in hdp_model.show_topics(formatted=True,num_topics=50,num_words=30):
            hdp_latent_topic_file.write(str(model))
            hdp_latent_topic_file.write("\n")
          
        hdp_data = pyLDAvis.gensim.prepare(hdp_model,corpus,dictionary)
        pyLDAvis.display(hdp_data)
        pyLDAvis.save_html(hdp_data, prof_topic_vis_file_nm+"hdp.html")
    except:
        traceback.print_exc()
        pass   

prof_nm_lst = []
try:
    for prof in open(prof_lst_file_nm,'rt', encoding='latin1'):
            prof_nm_lst.append("".join(prof.split()))
    
    writeProbEq(prof_nm_lst)
except:
    traceback.print_exc()
    
print("---END---")

