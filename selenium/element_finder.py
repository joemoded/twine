from selenium.webdriver.common.action_chains import ActionChains


def hover_over_element(self, element):
    ActionChains(self.driver).move_to_element(element).perform()


def find_element(self, locator):

    by = locator[0]
    value = locator[1]

    if by == 'TAG_NAME':
        return self.driver.find_element_by_tag_name(value)
    elif by == 'NAME':
        return self.driver.find_element_by_name(value)
    elif by == 'CLASS_NAME':
        return self.driver.find_element_by_class_name(value)
    elif by == 'CSS_SELECTOR':
        return self.driver.find_element_by_css_selector(value)
    elif by == 'LINK_TEXT':
        return self.driver.find_element_by_link_text(value)
    elif by == 'ID':
        return self.driver.find_element_by_id(value)
    elif by == 'NAME':
        return self.driver.find_(value)
    else:
        raise Exception("Unknown by in base find_element_by")

