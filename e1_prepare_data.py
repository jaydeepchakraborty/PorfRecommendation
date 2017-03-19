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
    for prof in open(prof_lst_file_nm,'rt', encoding='latin1'):
            prof_nm_lst.append("".join(prof.split()))
    
    for prof in prof_nm_lst:
        outfile = open(prof_pdf_path+prof+"/"+prof+".txt", 'wb')
        for file in os.listdir(prof_pdf_path+prof):
            if file.endswith(".pdf"):
                input=os.path.abspath(prof_pdf_path+prof+"/"+file)
                output=os.path.abspath(prof_pdf_path+prof+"/"+file)+".txt"
                #sudo apt-get install poppler-utils   ---> install with this command
                #which pdftotext ---> Get the path of  pdftotext
                subprocess.call("/usr/bin/pdftotext %s %s" % (input,output), shell=True)
                if os.path.exists(output):
                    with open(output, "rb") as pdfInfile:
                        outfile.write(pdfInfile.read())
                    pdfInfile.close()
            else:
                output=os.path.abspath(prof_pdf_path+prof+"/"+file)
                with open(output, "rb") as txtInfile:
                    outfile.write(txtInfile.read())
                txtInfile.close()
        outfile.close()
except Exception as e:
        print(e)
#-------------------------------------STOP----------------------------------------

print("---END---")