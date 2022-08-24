import importlib
import json
import os.path

import pytest
import jsonpickle

from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as file:
            target = json.load(file)
    return target

@pytest.fixture(scope = "session")
def app(request):
    global fixture 
    global target
    if fixture is None or not fixture.is_valid():
        browser = request.config.getoption("--browser")
        config = load_config(request.config.getoption("--target"))['web']
        fixture = Application(browser=browser, url=config['baseUrl'])
    fixture.session.ensure_login(username=config['username'], password=config['password'])
    return fixture
    
@pytest.fixture(scope = "session")
def db(request):
    config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(
        host=config['host'],
        name=config['name'],
        user=config['user'],
        password=config['password']
        )
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    def fin():
        global fixture 
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module(f"data.{module}").testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f"data/{file}.json")) as f:
        return jsonpickle.decode(f.read())