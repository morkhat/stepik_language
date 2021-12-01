
# selenium==4.0.0
# pytest==6.2.5

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='ru',
                     help="Choose language: ru, en, ...")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    #browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # задаем язык для браузера
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        #
        service = Service(r"путь до chromedriver")
        browser = webdriver.Chrome(options=options, service=service)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # задаем язык для браузера
        fp = webdriver.FirefoxOptions()
        fp.set_preference("intl.accept_languages", "{0}".format(user_language))
        #
        service = Service(r"путь до geckodriver")
        browser = webdriver.Firefox(firefox_profile=fp, service=service)
    #else:
        #raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()