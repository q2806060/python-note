from selenium import webdriver


# 1.创建浏览器对象
dirver = webdriver.PhantomJS()
# 2.利用浏览器对象的get方法发送请求
dirver.get("http://www.baidu.com/")
# 3.获取屏幕截图
dirver.save_screenshot("百度.png")
# 4.关闭浏览器
dirver.quit()