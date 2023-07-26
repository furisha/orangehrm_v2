from selenium import webdriver
import pytest

driver = None

@pytest.fixture(scope='session', autouse=True)
def setup():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
    return driver

# @pytest.fixture(scope='session', autouse=True)
# def setup():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, 'extras', [])

    if report.when == 'call':
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extras.append(pytest_html.extras.html(html))
        report.extra = extras


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)