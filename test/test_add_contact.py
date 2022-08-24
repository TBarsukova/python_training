from model.contact import Contact

    
def test_add_contact(app):
    app.open_home_page()
    app.contact.create(Contact(first_name="qwe", last_name="qwerty", address="qwe123"))
    app.return_to_home_page()


def test_add_empty_contact(app):
    app.open_home_page()
    app.contact.create(Contact(first_name="", last_name="", address=""))
    app.return_to_home_page()
