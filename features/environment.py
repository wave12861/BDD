from playwright.sync_api import sync_playwright

def before_all(context):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    context.browser = browser
    context.page = browser.new_page()
    context._playwright = playwright

def after_all(context):
    context.page.close()
    context.browser.close()
    context._playwright.stop()

def after_step(context, step):
    if step.status == "failed":
        context.page.screenshot(path=f"failed_{step.name}.png") 