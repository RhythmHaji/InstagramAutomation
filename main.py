# This is a demo automation for Instagram to log in to the app, take a photo, save to the gallery and then logout.
import unittest
from time import sleep

from appium import webdriver

import gallery_page
import home_page
import login_page
import options_page
import profile_page


class InstagramTest(unittest.TestCase):
    def setUp(self):
        desired_capabilities = {'platformName': 'Android', 'platformVersion': '7.1.2',
                        'deviceName': 'in-blr.headspin.io:8186', 'appPackage': 'com.instagram.android',
                        'appActivity': 'com.instagram.android.activity.MainTabActivity', 'autoGrantPermissions': 'true'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
        self.driver.implicitly_wait(10)
        self.timeout = 30

    def test_automation(self):

        login = login_page.LoginPage(self.driver)
        login.do_login()

        home = home_page.HomePage(self.driver)
        self.assertEqual(home.verify_home_page(), 'True')
        home.click_avatar_button()

        gallery = gallery_page.GalleryPage(self.driver)
        gallery.click_and_save_image()

        home = home_page.HomePage(self.driver)
        home.click_profile_icon()

        profile = profile_page.ProfilePage(self.driver)
        profile.click_more_options()

        log_out = options_page.OptionsPage(self.driver)
        log_out.do_logout()
        sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
