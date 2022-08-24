import pytest
from fixture.application import Application

fixture = None

@pytest.fixture(scope = "session")
def app(request):
    global fixture 
    if fixture is None or not fixture.is_valid():
        fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        global fixture 
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)


 