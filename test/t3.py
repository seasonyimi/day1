from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Firefox()
driver.get("https://www.baidu.com")

# driver.implicitly_wait(10)
#鼠标移动到“设置”按钮
mouse=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
#方法1
# driver.find_element_by_id("nr").click()
# time.sleep(3)
# driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()

# 方法2,通过索引
s=driver.find_element_by_id("nr")
Select(s).select_by_index(2)
s.click()

#方法3，select(只有当标签名称是select，选项标签为option的时候)
# e1=driver.find_element_by_id("nr")
# Select(e1).select_by_index(2)
# e1.click()

#点保存设置
driver.find_element_by_link_text("保存设置").click()
#alert弹窗的处理
a=driver.switch_to.alert    #却换到alert
t=a.text
print(t)
a.accept()     #点确认


time.sleep(5)
driver.quit()

