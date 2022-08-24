from model.group import Group

    
def test_modify_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.modify_group(0, Group(name="abc", header="def", footer="ghk"))
    app.return_to_home_page()
    app.session.logout()
