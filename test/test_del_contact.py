
def test_delete_first_contact(app):
    app.open_home_page()
    app.contact.delete_contact(0)
    app.return_to_home_page()
