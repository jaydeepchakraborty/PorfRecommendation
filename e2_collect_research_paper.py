from recoprofconst import *

prof_nm_lst = []
try:
    for prof in open(prof_lst_file_nm,'rt', encoding='utf8'):
            prof_nm_lst.append("".join(prof.split()))
    
    for prof in prof_nm_lst:
            chromedriver = driver_path
            os.environ[driver_name] = chromedriver
            prof_file = open(paper_nm_path+prof+".txt", 'r')
            lines = prof_file.readlines()
            for line in lines:
                try:
                    driver = webdriver.Chrome(chromedriver)
                    driver.get("https://scholar.google.com/")
                    search_fld_elmnt = WebDriverWait(driver, time_to_wait).until(lambda driver: driver.find_element_by_name("q"))
                    search_fld_elmnt.send_keys(line.split(" || ")[1])
                    search_btn = WebDriverWait(driver, time_to_wait).until(lambda driver: driver.find_element_by_name("btnG"))
                    search_btn.click()
                    pdf_fld_elmnt = WebDriverWait(driver, time_to_wait).until(lambda driver: driver.find_element_by_class_name("gs_ggsd"))
                    url = str(pdf_fld_elmnt.find_element_by_css_selector('a').get_attribute('href'))
                    urllib.request.urlretrieve(url, "/home/local/ASUAD/jchakra1/Desktop/pdfs/"+prof+"/"+str(line.split(" || ")[1])+".pdf")
                except:
                    traceback.print_exc()
                finally:
                    driver.quit()
                    print("hi")
except:
        traceback.print_exc()
#-------------------------------------STOP----------------------------------------

print("---END---")