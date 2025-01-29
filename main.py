from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from body_runner import driver

driver.get("https://chatik.hh.ru/?hhtmSource=chat_page&hhtmFrom=chat")
print(driver.title)

wait = WebDriverWait(driver, 10)

# Locate all chat cells
chat_cells_locator = (By.CLASS_NAME, 'oWKN7Ez___chat-cell')
wait.until(EC.presence_of_all_elements_located(chat_cells_locator))

# Locate the last message containing the "Отказ" text
message_locator = (
By.XPATH, './/div[contains(@class, "mnIHQ0E___last-message AkDJdek___last-message-color_red") and text()="Отказ"]')

# Try to find the message and click the corresponding chat cell
try:
    # Wait for the message to be present
    last_message_element = wait.until(EC.presence_of_element_located(message_locator))

    # Find the ancestor chat cell containing the last message
    chat_cell = last_message_element.find_element(By.XPATH, './ancestor::a[contains(@class, "oWKN7Ez___chat-cell")]')

    # Click on the chat cell
    chat_cell.click()
    print("Clicked on the chat cell with the 'Отказ' message!")

    # Wait for the menu button to be present after opening the chat
    menu_button_locator = (By.XPATH, '//button[@aria-label="menu" and @data-qa="chatik-chat-menu"]')
    menu_button = wait.until(EC.presence_of_element_located(menu_button_locator))

    # Click the menu button
    menu_button.click()
    print("Clicked on the menu button!")

    # Wait for the "Leave Chat" button to be present
    leave_chat_button_locator = (By.XPATH, '//button[@data-qa="chatik-chat-leave-chat"]')
    leave_chat_button = wait.until(EC.presence_of_element_located(leave_chat_button_locator))

    # Click the "Leave Chat" button
    leave_chat_button.click()
    print("Clicked on the 'Leave Chat' button!")

except Exception as e:
    print(f"Error: {e}")

# Optionally, you can add more actions or close the browser
# driver.quit()
