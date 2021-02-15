#coding:utf-8
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.implicitly_wait(10)

#获取title值
print(driver.title)
#获取元素属性值get_attribute("属性")
value=driver.find_element_by_id("su").get_attribute("value")
print(value)
# 判断元素是显示还是隐藏（返回布尔值）
d=driver.find_element_by_id("su").is_displayed()
print(d)
# 获取浏览器名称
print(driver.name)
# 获取元素size
s=driver.find_element_by_id("su").size
print(s)
#获取坐标
driver.save_screenshot('submit.png')
element=driver.find_element_by_id("su")
print(element.location)   #打印元素坐标
b