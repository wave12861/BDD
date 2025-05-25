from behave import given, when, then

@given('I am on the main page')
def step_impl(context):
    context.page.goto("https://demo-shop.example.com")

@when('I add the item "{item}" to the cart')
def step_impl(context, item):
    context.page.click(f'text="{item}"')
    context.page.click('button#add-to-cart')

@then('the item "{item}" should appear in the cart')
def step_impl(context, item):
    context.page.goto("https://demo-shop.example.com/cart")
    assert context.page.locator(f'text="{item}"').is_visible() 
    