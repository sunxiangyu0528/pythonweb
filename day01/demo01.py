from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as es
driver=webdriver.Chrome()
#在30秒内什么时候查到元素，什么时候走下面的代码
driver.implicitly_wait(30)
# driver.implicitly_wait()
driver.get("http://www.baidu.com")

driver.find_element_by_xpath(r'//input[@id="kw"]').send_keys("柠檬班")
# driver.find_element_by_id("kw").send_keys("刘若英")

driver.find_element_by_id("su").click()

windows=driver.window_handles
#隐式等待只能用来查找元素

driver.find_element_by_xpath('//*[contains(text(),"_腾讯课堂")]').click()

wait=WebDriverWait(driver,30)
wait.until(es.new_window_is_opened(windows))

# print(driver.window_handles)
driver.window_handles[-1]



driver.find_element_by_xpath('//h4[text()="华华老师"]').click()

time.sleep(5)

driver.quit()

# #显示等待
# wait=WebDriverWait(driver,timeout=30)
# #等待元素被加载
# wait.until(es.presence_of_element_located)



