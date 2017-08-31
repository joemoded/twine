from locators import email_client_elements
from element_finder import find_element
from page import BasePage


class EmailClient(BasePage):

    #these methods assume the "mark as read" and "mark as unread" buttons are unique and attached to each individual email and are
    #either hidden or visible, depending on the read status
    def update_to_read_status(self):
        mark_unread = find_element(self, email_client_elements['email_2_mark_as_unread'])
        mark_unread.click()
        #if button doesn't change return false
        if mark_unread.is_displayed():
            return False
        else:
            return True


    def update_to_unread_status(self):
        mark_read = find_element(self, email_client_elements['email_1_mark_as_read'])
        mark_read.click()
        #if button doesn't change return false
        if mark_read.is_displayed():
            return False
        else:
            return True


