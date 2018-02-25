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
        # Hermod hear about new website and he goes to it.
        # He open browser go to homepage.
        self.browser.get(self.live_server_url)

        # He notices the website title and header.
        self.assertIn('Letter', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Letter', header_text)

        # He create his new account by enterring his info.
        # He input his Username. Hermod really is good guys.
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

        # After that, he tries to logout.
        button = self.browser.find_element_by_id('id_logout')
        button.click()
        time.sleep(1)

        ## It is still the same web.

        # He then proceed to login.
        self.assertIn('Letter', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Letter', header_text)

        # He login by enter his username and password.
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

        # After he had logged in. Website greet him by his username.
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Hello', header_text)
        self.assertIn('hermod_isgood', header_text)

        # He remember that he has homework to do.
        # He sent letter in 1 hour later.
        button = self.browser.find_element_by_id('id_write_letter')
        button.click()

        inputbox = self.browser.find_element_by_id('id_subject')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter subject here.'
        )
        inputbox.send_keys("Finish the homework!")

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
        inputbox.send_keys(time.strftime("%d/%m/%Y %H:%M",
                            time.localtime(time.time() + 3600)))
        time.sleep(3)

        # After he finished writng, he send the letter.
        button = self.browser.find_element_by_id('id_send')
        button.click()
        time.sleep(0.5)

        # He wants to know that the letter has been saved
        # so he check the history.
        button = self.browser.find_element_by_id('id_history')
        button.click()

        table = self.browser.find_element_by_id('id_history_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('Finish the homework!', str([row.text for row in rows]))
        self.assertNotIn('I need to finish the homework.', str([row.text for row in rows]))
        time.sleep(1)

        # He has know that letter has been saved, but has the letter
        # been sent to his inbox yet? curious...

        self.fail("What's next boss?")
