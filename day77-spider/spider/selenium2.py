from selenium import webdriver
import time


driver = webdriver.PhantomJS()
driver.get("http://www.baidu.com/")
key = input("请输入要检索的内容：")
driver.find_element_by_id("kw").send_keys(key)
driver.find_element_by_id("su").click()
time.sleep(2)
driver.save_screenshot("result.png")
driver.quit()