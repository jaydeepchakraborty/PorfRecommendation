'''
This file is for data preparation
'''

from recoprofconst import *


#input='/Users/jaydeep/Desktop/test/third.pdf'
#output='/Users/jaydeep/Desktop/test/third.txt'
#subprocess.call("/usr/local/bin/pdftotext %s %s" % (input,output), shell=True)



#-------------------------------------START----------------------------------------
#This part concatenates all the documents for a particular professor
prof_nm_lst = []
try:
    for prof in open(prof_lst_file_nm,'rt', encoding='utf8'):
            prof_nm_lst.append("".join(prof.split()))
    
    for prof in prof_nm_lst:
        final_outfile = open(prof_pdf_path+prof+".dat", 'w+')
        final_outfile.seek(0)
        final_outfile.truncate()
        for file in os.listdir(prof_local_pdf_path+prof):
            if file.endswith(".pdf"):
                input=os.path.abspath(prof_local_pdf_path+prof+"/"+file)
                output=os.path.abspath(prof_local_pdf_path+prof+"/"+file)+".txt"
                #sudo apt-get install poppler-utils   ---> install with this command
                #which pdftotext ---> Get the path of  pdftotext
                subprocess.call("/usr/bin/pdftotext %s %s" % (input,output), shell=True)
                if os.path.exists(output):
                    with open(output, "r") as pdfInfile:
                        final_outfile.write(pdfInfile.read())
                    pdfInfile.close()
                if os.path.isfile(output):
                    os.remove(output)
        final_outfile.close()
except:
        traceback.print_exc()
#-------------------------------------STOP----------------------------------------

print("---END---")