
def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact(0)
    app.session.logout()
