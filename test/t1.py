#多窗口打开
#coding-utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
url="http://bj.ganji.com/"
driver.get(url)
# time.sleep(3)
#针对于当前页面的所有元素，却换页面或者页面卡顿无效
driver.implicitly_wait(10)  #10最大等待时间，定位元素时候有用，全局性

driver.find_element_by_link_text("租房").click()
time.sleep(5)
t=driver.title  #获取当前页title
print(t)        #光标聚焦在前一个页面
#获取当前窗口的handle
h1=driver.current_window_handle  #单个的
print(h1)
#获取所有窗口的handle
print("=========================")
all=driver.window_handles   #list对象
print(all)
#1.获取新窗口的handle
new_handle=all[-1]
print(new_handle)
#2.切换到新窗口的handle上
driver.switch_to.window(new_handle)
t2=driver.title
#回到第一个窗口
driver.switch_to.window(h1)
print(t2)

#关掉新的窗口
driver.close()

driver.quit()
