from selenium import webdriver
import unittest
import email_client
import os


class TestClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chromedriver = os.path.join(os.path.dirname(__file__), 'chromedriver')
        cls.driver = webdriver.Chrome(chromedriver)

    def setUp(self):
        self.driver.get("https://twine.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    # Confirm user is able to update email successfully
    def test_mark_as_unread(self):
        mark_as_unread = email_client.EmailClient(self).update_to_unread_status()
        assert mark_as_unread == True, 'Email status not updated'

    def test_mark_as_read(self):
        mark_as_read = email_client.EmailClient(self).update_to_read_status()
        assert mark_as_read, "Email status not updated"



if __name__ == "__main__":
    unittest.main()
