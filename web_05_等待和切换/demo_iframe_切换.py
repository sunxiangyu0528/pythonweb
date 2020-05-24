from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 设置隐式等待的超时时间
# 1， 如果在 30 s 之内找到了元素，那么什么时候找到元素，就什么时候运行下面的代码
# 超过 30s 没有找到，只能报错。不交 NoSuchElement,  TimeOutException.

driver.implicitly_wait(30)

driver.get("file:///D:/%E7%8F%AD%E7%BA%A7%E7%AE%A1%E7%90%86/python26%E6%9C%9F/web_05_%E7%AD%89%E5%BE%85%E5%92%8C%E5%88%87%E6%8D%A2/iframe_demo.html")

# iframe的切换
# 1, 索引， 从 0 开始
# # 2， name 属性
# # 3,  WebElement 对象
# # 4, locator ('xpath', '...')

driver.switch_to.frame('baidu')
# 等待
wait = WebDriverWait(driver, 20)
wait.until(EC.frame_to_be_available_and_switch_to_it( 'baidu' ))

driver.find_element_by_id('kw')
