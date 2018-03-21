from page import BasePage


class HomePage(BasePage):
    def verify_home_page(self):
        action_button = self.driver.find_element_by_id("com.instagram.android:id/action_bar_left_button")

        if action_button.is_displayed():
            print "Home Page verified"
            return "True"
        else:
            print "Login unsuccessful"
            return "False"

    def click_avatar_button(self):
        avatar_button = self.driver.find_element_by_id("com.instagram.android:id/avatar_image_view")
        avatar_button.click()
        print "avatar button clicked"

    def click_profile_icon(self):
        tab_icons = self.driver.find_elements_by_id("com.instagram.android:id/tab_icon")
        tab_icons[4].click()