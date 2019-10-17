from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.set_headless()

driver = webdriver.Chrome(options=options)
driver.get("https://www.douyu.com/directory/all")
while True:
    driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight)"
    )
    rList = driver.find_elements_by_class_name("layout-Cover-item")
    for r in rList:
        try:
            info = r.text.split("\n")
        except Exception as e:
            print(e)
            continue
        try:
            hot = info[2].strip()
            uname = info[3].strip()
        except Exception as e:
            print(e)
            continue
        d = {
            "hot":hot,
            "uname":uname,
        }
        with open("douyu.json","a",encoding="utf-8") as f:
            f.write(str(d)+'\n')
    if driver.page_source.find("dy-Pagination-disabled dy-Pagination-next") == -1:
        driver.find_element_by_class_name("dy-Pagination-next").click()
    else:
        break

driver.quit()
