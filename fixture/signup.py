import re
import time

class SignupHelper:

    def __init__(self, app):
        self.app = app

    def signup_new_user(self, username, email, password):
        driver = self.app.driver
        driver.get(self.app.base_url + "/signup_page.php")
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("email").send_keys(email)
        driver.find_element_by_css_selector('input[type="submit"]').click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmation_url(mail)

        driver.get(url)
        time.sleep(3)
        driver.get(url)
        driver.find_element_by_name("password").send_keys(password)
        time.sleep(3)
        driver.find_element_by_name("password_confirm").send_keys(password)
        time.sleep(3)
        driver.find_element_by_css_selector('input[value="Update User"]').click()

    def extract_confirmation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)
