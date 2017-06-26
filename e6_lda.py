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
        with open(prof_pdf_path + prof+".dat", 'r', encoding='latin-1') as prof_file:
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
        prof_lda_topic_file_nm = prof_topic_file_path+"lda"+'.txt'
        os.makedirs(os.path.dirname(prof_lda_topic_file_nm),exist_ok=True)
        lda_latent_topic_file = open(prof_lda_topic_file_nm, "w", encoding='latin1')
         
        lda_model = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=topics, 
                                           update_every=1, chunksize=10000, passes=20)
        for model in lda_model.show_topics(num_topics=topics,num_words=words,formatted=True):
            lda_latent_topic_file.write(str(model))
            lda_latent_topic_file.write("\n")
     
         
        lda_data = pyLDAvis.gensim.prepare(lda_model,corpus,dictionary)
        pyLDAvis.display(lda_data)
        pyLDAvis.save_html(lda_data, prof_topic_vis_file_nm+"lda.html")
    except:
        traceback.print_exc()
        pass
    
    
    #generating topic distribution for each model(LSA,LDA,HDP)
    prof_topic_dist_lda_file_nm = prof_topic_dist_path +"lda-topic-dist.txt"
    topic_dist_lda_file = open(prof_topic_dist_lda_file_nm, "w", encoding='latin1')
    
    for index,prof in enumerate(proflst):
        ##LDA topic distribution
        prof_topics_lda_dist, word_topics, phi_values = lda_model.get_document_topics(corpus[index],minimum_probability=0.00001, per_word_topics=True)
        topic_dist_lda_file.write(str(prof+","+str(prof_topics_lda_dist)))
        topic_dist_lda_file.write("\n")
   


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

