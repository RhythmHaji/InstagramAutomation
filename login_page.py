from page import BasePage


class LoginPage(BasePage):
    def do_login(self):
        login_button = self.driver.find_element_by_id("com.instagram.android:id/log_in_button")
        login_button.click()

        user_name = self.driver.find_element_by_id("com.instagram.android:id/login_username")
        user_name.click()
        user_name.clear()
        user_name.send_keys("automationqa77")
        print "username entered"
        self.driver.back()

        password = self.driver.find_element_by_id("com.instagram.android:id/password")
        password.click()
        password.clear()
        password.send_keys("asdfasdf#12")
        print "password entered"

        log_in_button = self.driver.find_element_by_id("com.instagram.android:id/button_text")
        log_in_button.click()
        print "log in button clicked"