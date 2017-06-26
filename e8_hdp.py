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
        with open(prof_pdf_path + prof +".dat", 'r', encoding='latin-1') as prof_file:
                prof_doc_set.append(prof_file.read().replace('\n', ' '))
    
    
    #list for tokenized documents in loop
    prof_texts = []
    for index,prof_doc in enumerate(prof_doc_set):
        #print(index)
        
        #clean and tokenize document
        raw_data = prof_doc.lower()
        tokens = tokenizer.tokenize(raw_data)
    
        
        #removing stop words from tokens
        stopped_tokens_tmp1 = [i for i in tokens if not i.strip() in en_stop]
        
        #removing non english words from tokens
        stopped_tokens_tmp2 = [i for i in stopped_tokens_tmp1 if isEnglish(i.strip())]
        
        #removing digits from tokens
        stopped_tokens = [i for i in stopped_tokens_tmp2 if not i.strip().isdigit()]
        
        #stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        
        #add tokens to list
        prof_texts.append(stemmed_tokens)
    
    #turn our tokenized documents into a id <-> term dictionary    
    dictionary = corpora.Dictionary(prof_texts)    
    #convert tokenized documents into document - term matrix
    corpus = [dictionary.doc2bow(text) for text in prof_texts]
    
    
    #Creating folder for saving visual files
    prof_topic_vis_file_nm = prof_topic_vis_path
    os.makedirs(os.path.dirname(prof_topic_vis_file_nm),exist_ok=True)
    
    try:
        prof_hdp_topic_file_nm = prof_topic_file_path+"hdp"+'.txt'
        os.makedirs(os.path.dirname(prof_hdp_topic_file_nm),exist_ok=True)
        hdp_latent_topic_file = open(prof_hdp_topic_file_nm, "w", encoding='latin1')
         
        hdp_model = models.hdpmodel.HdpModel(corpus, id2word=dictionary)
        for model in hdp_model.show_topics(formatted=True,num_topics=topics,num_words=words):
            hdp_latent_topic_file.write(str(model))
            hdp_latent_topic_file.write("\n")
        print("hdp.txt is done")  
        hdp_data = pyLDAvis.gensim.prepare(hdp_model,corpus,dictionary)
        pyLDAvis.display(hdp_data)
        pyLDAvis.save_html(hdp_data, prof_topic_vis_file_nm+"hdp.html")
        print("hdp.html is done")
    except:
        traceback.print_exc()
        pass 
    
    
    #generating topic distribution for each model(LSA,LDA,HDP)
    prof_topic_dist_hdp_file_nm = prof_topic_dist_path +"hdp-topic-dist.txt"
    topic_dist_hdp_file = open(prof_topic_dist_hdp_file_nm, "w", encoding='latin1')
    
    for index,prof in enumerate(proflst):
        ##HDP topic distribution
        hdp_to_lda_ldamodel = hdp_model.suggested_lda_model()
        prof_topics_hdp_dist, word_topics, phi_values = hdp_to_lda_ldamodel.get_document_topics(corpus[index],minimum_probability=0.00001,per_word_topics=True)
        topic_dist_hdp_file.write(str(prof+","+str(prof_topics_hdp_dist)))
        topic_dist_hdp_file.write("\n")

    print("hdp-topic-dist.txt is done")


prof_nm_lst = []
start_time = time.time()
try:
    for prof in open(prof_lst_file_nm,'rt', encoding='latin1'):
            prof_nm_lst.append("".join(prof.split()))
    
    writeProbEq(prof_nm_lst)
except:
    traceback.print_exc()

print("--- %s seconds ---" % (time.time() - start_time))   
print("---END---")

