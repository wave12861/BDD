from behave import given, when, then
from playwright.sync_api import expect

@given('I am on the Google page')
def step_impl(context):
    context.page.goto("https://www.google.com")
    # Accept cookies if the dialog appears
    try:
        context.page.click('button:has-text("Accept all")')
    except:
        pass  # Cookie dialog might not appear

@when('I search for "{search_text}"')
def step_impl(context, search_text):
    context.page.fill('textarea[name="q"]', search_text)
    context.page.press('textarea[name="q"]', 'Enter')

@then('I see search results')
def step_impl(context):
    # Wait for search results to appear
    context.page.wait_for_selector('#search')

@then('the first result contains "{text}"')
def step_impl(context, text):
    # Get the first search result
    first_result = context.page.locator('#search a').first
    # Check if it contains the expected text
    assert text.lower() in first_result.text_content().lower() 