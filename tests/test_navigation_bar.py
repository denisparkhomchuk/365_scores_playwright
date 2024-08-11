import pytest
import allure

from pages.page_main import MainPage
from playwright.sync_api import expect, Page


@pytest.mark.parametrize('section_to_goto,expected_page_title', [
    ('Каталог', 'Каталог Onlíner'),
    ('Дома и квартиры', 'Купить квартиру в Минске')
])
@allure.title("Onliner Navigation bar test")
def test_navigation_bar(
        section_to_goto,
        expected_page_title,
        page: Page,
        page_main: MainPage) -> None:
    page_main.load()
    page_main.navigation_bar.goto(section_to_goto)
    current_page = page_main.page
    current_page.wait_for_load_state()
    expect(current_page).to_have_title(expected_page_title)
