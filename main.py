from infrastructure.browser import get_driver
from interfaces.chat_repository import ChatRepository
from use_cases.chat_processing import ChatProcessor

driver = get_driver()
driver.get("https://chatik.hh.ru/?hhtmSource=chat_page&hhtmFrom=chat")
chat_repository = ChatRepository(driver)
chat_repository.set_to_unread()
chat_processor = ChatProcessor(chat_repository)
while True:
    chat_processor.process_chats()
# driver.quit()  # Uncomment to close the driver after execution