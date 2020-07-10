import pytest
import json
import os.path
from osve.fixture.applicaton import Application
import importlib
import jsonpickle
from osve.fixture.db import DbFixture

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
#    fixture = Application()
#    fixture.session.login(username="admin", passw="secret")
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])

    fixture.session.ensure_login(username=web_config["username"], passw=web_config["password"])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--browser", action="store", default="firefox")

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

#fix needed to file path !!!
def load_from_json(file):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\%s.json" % file)) as f:
        return jsonpickle.decode(f.read())