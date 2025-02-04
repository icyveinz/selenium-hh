from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys
from enitites.chat import Chat


class ChatRepository:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_to_unread(self):
        sleep(5)
        filter_div_locator = (By.CSS_SELECTOR, 'div.BUagpy6___filter-item')
        filter_div = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(filter_div_locator))
        filter_div.click()

    def get_all_chats(self):
        chat_cells_locator = (By.CLASS_NAME, 'oWKN7Ez___chat-cell')
        chat_cells = self.wait.until(EC.presence_of_all_elements_located(chat_cells_locator))
        return [Chat(cell) for cell in chat_cells]

    def leave_chat(self):
        menu_button_locator = (By.XPATH, '//button[@aria-label="menu" and @data-qa="chatik-chat-menu"]')
        menu_button = self.wait.until(EC.presence_of_element_located(menu_button_locator))
        menu_button.click()

        leave_chat_button_locator = (By.XPATH, '//button[@data-qa="chatik-chat-leave-chat"]')
        leave_chat_button = self.wait.until(EC.presence_of_element_located(leave_chat_button_locator))
        leave_chat_button.click()

    def scroll_down(self):
        scrollable_element_locator = (By.CLASS_NAME, 'VKJD3HM___chats')
        scrollable_element = self.wait.until(EC.presence_of_element_located(scrollable_element_locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(scrollable_element).click().send_keys(Keys.END).perform()