from page import BasePage


class OptionsPage(BasePage):
    def do_logout(self):
        log_out = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().'
            'text("Log Out").instance(0));')
        log_out.click()
        print "log out clicked"

        confirm_logout = self.driver.find_element_by_id("com.instagram.android:id/button_positive")
        confirm_logout.click()
        print "automation over"