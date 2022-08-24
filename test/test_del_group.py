from model.group import Group

def test_delete_first_group(app):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))
    app.group.delete_group(0)
