import pytest
from unittest.mock import MagicMock, patch
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from enitites.chat import Chat
from interfaces.chat_repository import ChatRepository



@pytest.fixture
def mock_driver():
    driver = MagicMock(spec=WebDriver)
    return driver


@pytest.fixture
def chat_repo(mock_driver):
    return ChatRepository(mock_driver)


def test_set_to_unread(chat_repo, mock_driver):
    mock_element = MagicMock(spec=WebElement)
    with patch("time.sleep"), patch("selenium.webdriver.support.ui.WebDriverWait.until") as mock_wait:
        mock_wait.return_value = mock_element

        chat_repo.set_to_unread()

    mock_element.click.assert_called_once()



def test_get_all_chats(chat_repo, mock_driver):
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_elements.return_value = [mock_element, mock_element]

    chats = chat_repo.get_all_chats()

    assert len(chats) == 2
    assert all(isinstance(chat, Chat) for chat in chats)


def test_leave_chat(chat_repo, mock_driver):
    mock_menu_button = MagicMock(spec=WebElement)
    mock_leave_button = MagicMock(spec=WebElement)

    mock_driver.find_element.side_effect = [mock_menu_button, mock_leave_button]

    chat_repo.leave_chat()

    assert mock_menu_button.click.call_count == 1
    assert mock_leave_button.click.call_count == 1
