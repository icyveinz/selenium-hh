from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from body_runner import driver

driver.get("https://chatik.hh.ru/?hhtmSource=chat_page&hhtmFrom=chat")
print(driver.title)

wait = WebDriverWait(driver, 10)

# Loop to process all chats with the "Отказ" message
while True:
    try:
        # Locate all chat cells
        chat_cells_locator = (By.CLASS_NAME, 'oWKN7Ez___chat-cell')
        chat_cells = wait.until(EC.presence_of_all_elements_located(chat_cells_locator))

        # Iterate through all chat cells
        for chat_cell in chat_cells:
            # Locate the last message with "Отказ"
            message_locator = (
                By.XPATH,
                './/div[contains(@class, "mnIHQ0E___last-message AkDJdek___last-message-color_red") and text()="Отказ"]')
            try:
                last_message_element = chat_cell.find_element(By.XPATH, message_locator[1])

                # Click on the chat cell containing the 'Отказ' message
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

                # Wait for the page to reload or update before continuing to the next chat
                wait.until(EC.presence_of_all_elements_located(chat_cells_locator))

            except Exception as inner_e:
                print(f"No 'Отказ' message in this chat. Error: {inner_e}")

        # After processing all chat cells, refresh to get any new chats if needed
        driver.refresh()
        print("Refreshing to get new chat data.")

    except Exception as e:
        print(f"Error during chat processing: {e}")
        break

# Optionally, you can close the driver when done
# driver.quit()

