from behave import given, when, then
from playwright.sync_api import expect

@given('I am on the login page')
def step_impl(context):
    context.page.goto("https://the-internet.herokuapp.com/login")
    # Wait for the page to load
    context.page.wait_for_selector('#username')

@when('I enter username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.page.fill('#username', username)
    context.page.fill('#password', password)

@when('I click the login button')
def step_impl(context):
    context.page.click('button[type="submit"]')

@then('I should see the success message')
def step_impl(context):
    # Wait for and verify the success message
    flash_message = context.page.locator('.flash.success')
    expect(flash_message).to_contain_text("You logged into a secure area!")

@then('I should be logged in successfully')
def step_impl(context):
    # Verify we're on the secure area page
    expect(context.page).to_have_url("https://the-internet.herokuapp.com/secure")
    # Verify the secure area heading is visible
    expect(context.page.locator('h2')).to_contain_text("Secure Area") 