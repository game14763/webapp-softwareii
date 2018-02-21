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

    def test_user_can_send_letter(self):
        # Hermod hear about new website he goes to it.
        # He open browser go to homepage.
        self.browser.get(self.live_server_url)

        # He notices the website title and header.
        self.assertIn('Letter', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Letter', header_text)

        # He create his new account by enterring his info.
        # He inout his Username. Hermod really is good guys.
        inputbox = self.browser.find_element_by_id('id_regis_username')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Username'
        )
        inputbox.send_keys('hermod_isgood')

        # He then enter his Emails. (Is he some kind of Django staff?)
        inputbox = self.browser.find_element_by_id('id_regis_email')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Email'
        )
        inputbox.send_keys('hermod@django.com')

        # He then choose his hard-to-guess Password. (Thats REALLY hard)
        inputbox = self.browser.find_element_by_id('id_regis_password')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Password'
        )
        inputbox.send_keys('donthackme')
        time.sleep(3)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)

        # After that he tries to logout.
        # He find no use now. So he decide to close the browser.
        button = self.browser.find_element_by_id('id_logout')
        button.click()
        time.sleep(3)

        # def test_user_can_send_letter(self):
        # Hermod want to send a letter to self in next hour.
        # He open browser go to homepage.
        # self.browser.get(self.live_server_url)

        # He notices the website title and header.
        # It is still the same web.
        self.assertIn('Letter', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Letter', header_text)

        # Then he login by enter his username and password
        inputbox = self.browser.find_element_by_id('id_login_username')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Username'
        )
        inputbox.send_keys('hermod_isgood')

        inputbox = self.browser.find_element_by_id('id_login_password')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Password'
        )
        inputbox.send_keys('donthackme')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # After He logged in he have seen his username in header
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('hermod_isgood', header_text)

        # He want to send letter so he clicked the send letter button.
        button = self.browser.find_element_by_id('id_write_letter')
        button.click()

        inputbox = self.browser.find_element_by_id('id_subject')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter subject here.'
        )
        inputbox.send_keys("homework")
        
        inputbox = self.browser.find_element_by_id('id_message')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter message here.'
        )
        inputbox.send_keys("I need to finish the homework.")

        inputbox = self.browser.find_element_by_id('datetimepicker')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'dd/mm/yyyy hh:mm'
        )
        inputbox.send_keys(time.strftime("%d/%m/%Y %H:%M",time.localtime(time.time() + 3600)))

        button = self.browser.find_element_by_id('id_send')
        button.click()

        button = self.browser.find_element_by_id('id_history')
        button.click()

        table = self.browser.find_element_by_id('id_history_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('homework', str([row.text for row in rows]))
        self.assertNotIn('I need to finish the homework.', str([row.text for row in rows]))

