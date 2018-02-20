from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):  
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):  
        self.browser.quit()

    def test_user_can_register_and_logout(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Letter', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Letter', header_text)

        inputbox = self.browser.find_element_by_id('id_regis_username')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Username'
        )
        inputbox.send_keys('Hermod_isgood')

        inputbox = self.browser.find_element_by_id('id_regis_email')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Email'
        )
        inputbox.send_keys('hermod@django.com')


        inputbox = self.browser.find_element_by_id('id_regis_password')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Password'
        )
        inputbox.send_keys('donthackme')
        time.sleep(3)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        button = self.browser.find_element_by_id('id_logout')
        button.click()
        time.sleep(3)

    def test_user_can_send_letter(self):
        # Hermod want to send a letter to self in next hour.
        # He open browser go to homepage.
        self.browser.get(self.live_server_url)
        
        # He notices the website title and header.
        self.assertIn('Letter', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Letter', header_text)

        # Then he login by enter username and password
        inputbox = self.browser.find_element_by_id('id_login_username')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Username'
        )
        inputbox.send_keys('Hermod_isgood')

        inputbox = self.browser.find_element_by_id('id_login_password')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Password'
        )
        inputbox.send_keys('donthackme')
        inputbox.send_keys(Keys.ENTER)

        # After He logged in he have seen his username in header
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('hermod_isgood', header_text)

        # He want to send letter so he clicked the send letter button.
        button = self.browser.find_element_by_id('id_write_letter')
        button.click()
        time.sleep(5)
