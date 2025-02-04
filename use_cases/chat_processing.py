class ChatProcessor:
    def __init__(self, chat_repository):
        self.chat_repository = chat_repository

    def process_chats(self):
        try:
            chats = self.chat_repository.get_all_chats()
            for chat in chats:
                if chat.has_rejection_message():
                    chat.click()
                    self.chat_repository.leave_chat()
            self.chat_repository.scroll_down()
        except Exception as e:
            print(f"Error during chat processing: {e}")