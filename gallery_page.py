from page import BasePage


class GalleryPage(BasePage):

    def click_and_save_image(self):
        camera_button = self.driver.find_element_by_id("com.instagram.android:id/camera_shutter_button")
        camera_button.click()
        print "camera button clicked"

        camera_save = self.driver.find_element_by_id("com.instagram.android:id/camera_save_button")
        camera_save.click()
        print "camera save button clicked"
        self.driver.back()
        self.driver.back()