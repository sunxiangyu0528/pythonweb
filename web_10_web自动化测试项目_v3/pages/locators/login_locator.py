from selenium.webdriver.common.by import By


class LoginLocator:
    user_locator = (By.NAME, 'phone')
    pwd_locator = (By.NAME, 'password')
    btn_locator = (By.XPATH, "//button[@class='btn btn-special']")
    error_info_locator = (By.XPATH, "//div[@class='form-error-info']")
    invalid_info_locator = (By.CLASS_NAME, "layui-layer-content")