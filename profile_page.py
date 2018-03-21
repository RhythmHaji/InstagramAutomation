from page import BasePage


class ProfilePage(BasePage):
    def click_more_options(self):
        more_options = self.driver.find_element_by_id("com.instagram.android:id/action_bar_overflow_icon")
        more_options.click()
        print "more options clicked"