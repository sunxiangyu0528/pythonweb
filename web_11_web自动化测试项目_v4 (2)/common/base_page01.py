class BasePage:

    def __init__(self,driver):
        self.driver=driver

    def get_element(self,locator):
        e = self.driver.find_element(*locator)