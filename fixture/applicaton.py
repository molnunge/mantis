from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "ie":
            self.driver = webdriver.Ie()
        else:
            raise ValueError("unrecognized browser %s" % browser)
#        self.driver.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.base_url=base_url

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False

    def open_home_page(self, driver):
        driver = self.driver
        driver.get(self.base_url)
            #("http://localhost/addressbook")

    def destroy(self):
        self.driver.quit()