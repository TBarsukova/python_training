import pytest
from fixture.application import Application

fixture = None

@pytest.fixture(scope = "session")
def app(request):
    global fixture 
    if fixture is None or not fixture.is_valid():
        browser = request.config.getoption("--browser")
        url = request.config.getoption("--url")
        fixture = Application(browser=browser, url=url)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        global fixture 
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--url", action="store", default="http://localhost/addressbook/")
