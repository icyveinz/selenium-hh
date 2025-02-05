import pytest
from unittest.mock import MagicMock, patch
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from enitites.chat import Chat
from interfaces.chat_repository import ChatRepository



@pytest.fixture
def mock_driver():
    """Mock Selenium WebDriver."""
    driver = MagicMock(spec=WebDriver)
    return driver


@pytest.fixture
def chat_repo(mock_driver):
    """Fixture for ChatRepository instance."""
    return ChatRepository(mock_driver)


def test_set_to_unread(chat_repo, mock_driver):
    """Test set_to_unread clicks the correct filter div."""
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_element.return_value = mock_element

    with patch("time.sleep"):  # To avoid actual sleep calls
        chat_repo.set_to_unread()

    mock_driver.find_element.assert_called_with(By.CSS_SELECTOR, 'div.BUagpy6___filter-item')
    mock_element.click.assert_called_once()


def test_get_all_chats(chat_repo, mock_driver):
    """Test get_all_chats returns a list of Chat objects."""
    mock_element = MagicMock(spec=WebElement)
    mock_driver.find_elements.return_value = [mock_element, mock_element]

    chats = chat_repo.get_all_chats()

    assert len(chats) == 2
    assert all(isinstance(chat, Chat) for chat in chats)


def test_leave_chat(chat_repo, mock_driver):
    """Test leave_chat clicks the menu and leave buttons."""
    mock_menu_button = MagicMock(spec=WebElement)
    mock_leave_button = MagicMock(spec=WebElement)

    mock_driver.find_element.side_effect = [mock_menu_button, mock_leave_button]

    chat_repo.leave_chat()

    assert mock_menu_button.click.call_count == 1
    assert mock_leave_button.click.call_count == 1


def test_scroll_down(chat_repo, mock_driver):
    """Test scroll_down performs scrolling action."""
    mock_scrollable_element = MagicMock(spec=WebElement)
    mock_driver.find_element.return_value = mock_scrollable_element

    with patch("selenium.webdriver.common.action_chains.ActionChains") as MockActionChains:
        mock_actions = MockActionChains.return_value
        chat_repo.scroll_down()

        MockActionChains.assert_called_once_with(mock_driver)
        mock_actions.move_to_element.assert_called_with(mock_scrollable_element)
        mock_actions.click.assert_called_once()
        mock_actions.send_keys.assert_called_once()
        mock_actions.perform.assert_called_once()
