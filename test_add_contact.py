# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="qwe", last_name="qwerty", address="qwe123"))
    app.return_to_home_page()
    app.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", last_name="", address=""))
    app.return_to_home_page()
    app.logout()
