
def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_group(0)
    app.session.logout()
