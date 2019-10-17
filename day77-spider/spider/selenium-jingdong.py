from selenium import webdriver
import csv
import time

url = "https://www.jd.com"

key = input("请输入搜索的物品：")



driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_class_name("text").send_keys(key)
driver.find_element_by_class_name("button").click()
time.sleep(2)
# driver.save_screenshot("test.png")


for i in range(5):
    # 执行JS脚本，把进度条拉到最底部
    driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight)"
    )
    rList = driver.find_elements_by_class_name("gl-item")
    for r in rList:
        info = r.text.split("\n")
        price = info[0].strip()
        name = info[1].strip()
        commit = info[2].strip()
        shop = info[3].strip()

        d = {
            "price":price,
            "name":name,
            "commit":commit,
            "shop":shop,
        }
        with open("jingdong.json", "a",encoding="utf-8") as f:
            f.write(str(d)+'\n')
    
    if driver.page_source.find("pn-next disable") == -1:
        driver.find_element_by_class_name("pn-next").click()
        time.sleep(2)
    else:
        break

driver.quit()
