# another testing module is playwright
# pip3 install playwright
# pip3 install pytest-playwright
# playwright install
# to test with playwright - we will use https://demo.applitools.com
# to run the test headless (no gui - just test) - python3 -m pytest tau_pytest/tests/test_ui.py
# to see it running - python3 -m pytest tau_pytest/tests/test_ui.py --headed --slowmo 1000

import pytest
import re

from playwright.sync_api import Page, expect

@pytest.mark.ui
@pytest.mark.acme_bank
def test_acme_bank_login(page: Page):

    # Arrange - load the page
    page.goto('https://demo.applitools.com')

    # Act - interact with elements on the page
    page.locator('id=username').fill('andy')
    page.locator('id=password').fill('i<3pandas')
    page.locator('id=log-in').click()

    # Assert - check if the main page loaded correctly
    # Playwright uses the expect and not the assert as pytest
    # because the expect wait for the elements to be ready
    # this is called Web First Assertions
    expect(page.locator('div.logo-w')).to_be_visible()
    expect(page.locator('ul.main-menu')).to_be_visible()
    expect(page.get_by_text('Add Account')).to_be_visible()
    expect(page.get_by_text('Make Payment')).to_be_visible()
    expect(page.get_by_text('View Statement')).to_be_visible()
    expect(page.get_by_text('Request Increase')).to_be_visible()
    expect(page.get_by_text('Pay Now')).to_be_visible()



