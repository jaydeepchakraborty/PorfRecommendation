from recoprofconst import *

# chromedriver = driver_path
# os.environ[driver_name] = chromedriver
chromeOptions = webdriver.ChromeOptions()
prefs = {"plugins.always_open_pdf_externally":True}
chromeOptions.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(chrome_options=chromeOptions)
try:
    driver.get("http://www.sciencedirect.com/science/article/pii/S0377221707010508")
#     driver.switch_to_frame(0);
    elemnt = driver.execute_script("return document.querySelector(\"a[id='pdfLink']\")")
    print(elemnt)
    if not (elemnt is None):
        driver.execute_script("arguments[0].click();",elemnt)
    time.sleep(10)
finally:
    driver.quit()