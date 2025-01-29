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
except Exception as e:
    print(f"Error: {e}")

# Optionally, you can add more actions or close the browser
# driver.quit()
