from selenium import webdriver

# Chrome设置无界面模式

options = webdriver.ChromeOptions()
options.set_headless()

driver = webdriver.Chrome(options=options)
driver.get("https://www.qiushibaike.com/text/")
rone = driver.find_element_by_class_name("content")
print(rone)
rmany = driver.find_elements_by_class_name("content")
for r in rmany:
    print(r.text)   
driver.quit()