from selenium.common.exceptions import NoSuchElementException

class Chat:
    def __init__(self, element):
        self.element = element

    def has_rejection_message(self):
        try:
            self.element.find_element("xpath", './/div[contains(@class, "mnIHQ0E___last-message AkDJdek___last-message-color_red") and text()="Отказ"]')
            return True
        except NoSuchElementException:
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

    def click(self):
        self.element.click()