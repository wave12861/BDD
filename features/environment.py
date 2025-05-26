from playwright.sync_api import sync_playwright

def before_all(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()

def after_all(context):
    context.browser.close()

def after_step(context, step):
    if step.status == "failed":
        context.page.screenshot(path=f"failed_{step.name}.png") 