from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 设置隐式等待的超时时间
# 1， 如果在 30 s 之内找到了元素，那么什么时候找到元素，就什么时候运行下面的代码
# 超过 30s 没有找到，只能报错。不交 NoSuchElement,  TimeOutException.

driver.implicitly_wait(30)

driver.get("file:///D:/%E7%8F%AD%E7%BA%A7%E7%AE%A1%E7%90%86/python26%E6%9C%9F/web_05_%E7%AD%89%E5%BE%85%E5%92%8C%E5%88%87%E6%8D%A2/iframe_demo.html")

e = driver.find_element_by_id("p")
e.click()
# 切换到弹框, 没有括号
my_alert = driver.switch_to.alert

# 等待
# wait = WebDriverWait(driver, 30)
# my_alert = wait.until(EC.alert_is_present)


# 点击弹框的确认按钮
my_alert.accept()
# 取消
# my_alert.dismiss()
