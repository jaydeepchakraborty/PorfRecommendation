from recoprofconst import *


prof_nm_lst = []

for prof in open(prof_lst_file_nm,'rt', encoding='utf8'):
        prof_nm_lst.append(prof.strip())

for prof in prof_nm_lst:
    print(prof)
    print("------------------------------------")
#     file_nm = "".join(prof.split())
#     print(file_nm)
    try:
#         with open(paper_nm_path+file_nm+".txt",'w', encoding='utf8') as prof_file:
            prof_lst = dblp_scrapper.search(prof)
            if prof_lst:
                for prof_infos in prof_lst:
                    print(len(prof_infos.publications))
#                     prof_pubs = prof_infos.publications
#                     for prof_pub in prof_pubs:
#                         prof_pub_info = str(prof_pub.ee) + " || " + str(prof_pub.title + " || " + str(prof_pub.authors))
#                         print(prof_pub_info)
#                         prof_file.write(prof_pub_info)
#                         prof_file.write("\n")  
                    
#             prof_file.close()
            time.sleep(60*3) # delays for 3 minutes
    except:
        traceback.print_exc()
#-------------------------------------STOP----------------------------------------

print("---END---")           
            



# authors = search('Hasan Davulcu')
# michael = authors[0]
# print(len(michael.publications))
# print (michael.publications[0].title)
# print (michael.publications[0].ee)