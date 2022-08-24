from model.group import Group

    
def test_modify_first_group(app):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))
    app.group.modify_group(0, Group(name="abc", header="def", footer="ghk"))

