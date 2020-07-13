class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        driver = self.app.driver
        self.app.open_home_page(driver)
        driver.find_element_by_name("username").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_css_selector("input[type='submit']").click()

    def logout(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        driver = self.app.driver
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        driver = self.app.driver
        # some wierd shit with not working of next tests if there is no preliminary accessing to this
        # variables
        a = self.is_logged_in()
#        print("This a text is to show variable value " + str(a))
#        self.login(username, passw)
        if self.is_logged_in():
            if self.is_logged_in_as(username):
#                b = self.is_logged_in_as(username)
#                print("This b text is to show variable value " + str(b))
                return
            else:
                self.logout()
        self.login(username, password)

    def is_logged_in(self):
        driver = self.app.driver
        return len(driver.find_elements_by_link_text("Logout")) > 0

    def is_logged_in_as(self, username):
        driver = self.app.driver
        return self.get_logged_user() == username

    def get_logged_user(self):
        driver = self.app.driver
        return driver.find_element_by_id("logged-in-user").text