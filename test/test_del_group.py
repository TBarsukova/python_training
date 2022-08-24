from model.group import Group

def test_delete_first_group(app):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))
    old_groups = app.group.get_group_list()
    app.group.delete_group(0)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups = old_groups[1:]
    assert sorted(old_groups) == sorted(new_groups)


