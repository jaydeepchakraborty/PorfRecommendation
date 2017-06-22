from recoprofconst import *

url_1 = "ieee"
url_2 = "springer"
url_3 = "acm"
url_4 = "sciencedirect"
url_5 = "arxiv"
url_6 = "aaai"

prof_nm_lst = []
try:
    for prof in open(prof_lst_file_nm,'rt', encoding='utf8'):
            prof_nm_lst.append("".join(prof.split()))
    
    with open(err_file,"a") as errfile:
        for prof in prof_nm_lst:
                errfile.write("=============== "+prof+" ===========================")
                errfile.write("\n")
                chromeOptions = webdriver.ChromeOptions()
                prefs = {"plugins.always_open_pdf_externally":True,"download.default_directory":"/home/local/ASUAD/jchakra1/Desktop/pdfs/"+prof+"//"}
                chromeOptions.add_experimental_option("prefs", prefs)
                prof_file = open(paper_nm_path+prof+".txt", 'r')
                lines = prof_file.readlines()
                for line in lines:
                    try:
                        driver = webdriver.Chrome(chrome_options=chromeOptions)
                        driver.get(line.split(" || ")[0])
                        time.sleep(10)
                        current_url = WebDriverWait(driver, time_to_wait).until(lambda driver:driver.current_url)
                        
                        if url_1 in current_url:
                            pdf_btn = WebDriverWait(driver, time_to_wait).until(lambda driver: driver.find_element_by_xpath("//a[@ng-if='ft.article.fullTextAccess']"))
                            pdf_btn.click()
                            time.sleep(15)
                        elif url_2 in current_url:
                            elemnt = driver.execute_script("return document.querySelector(\"a[title='Download this paper in PDF format']\")")
                            if not (elemnt is None):
                                driver.execute_script("arguments[0].click();",elemnt)
                            else:
                                elemnt = driver.execute_script("return document.querySelector(\"a[title='Download this article in PDF format']\")")
                                if not (elemnt is None):
                                    driver.execute_script("arguments[0].click();",elemnt)
                            time.sleep(15)
                        elif url_3 in current_url:
                            pdf_btn = WebDriverWait(driver, time_to_wait).until(lambda driver: driver.find_element_by_xpath("//a[@name='FullTextPDF']"))
                            pdf_btn.click()
                            time.sleep(15)
                        elif url_4 in current_url:
                            elemnt = driver.execute_script("return document.querySelector(\"a[id='pdfLink']\")")
                            if not (elemnt is None):
                                driver.execute_script("arguments[0].click();",elemnt)
                            else:
                                errfile.write("error happened :- "+ line.split(" || ")[0])
                            time.sleep(15) 
                        elif url_5 in current_url:
                            pdf_btn = WebDriverWait(driver, time_to_wait).until(lambda driver: driver.find_element_by_xpath("//a[@accesskey='f']"))
                            pdf_btn.click()
                            time.sleep(15)
                        elif url_6 in current_url:
                            driver.switch_to_frame(0);
                            pdf_btn = WebDriverWait(driver, time_to_wait).until(EC.presence_of_element_located((By.CLASS_NAME, "action")))
                            pdf_btn.click()
                            time.sleep(15)
                        else:
                            errfile.write("not downloaded :- "+ line.split(" || ")[0])
                            errfile.write("\n")
                    except:
                        errfile.write("error happened :- "+ line.split(" || ")[0])
                        errfile.write("\n")
                        errfile.write(traceback.format_exc())
                        errfile.write("\n")
                    finally:
                        driver.quit()
                        time.sleep(15) # delays for 15 second
                time.sleep(1*60)
except:
        traceback.print_exc()
#-------------------------------------STOP----------------------------------------

print("---END---")