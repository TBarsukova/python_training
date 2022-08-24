from model.group import Group

def test_delete_first_group(app):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))
    old_groups = app.group.get_group_list()
    app.group.delete_group(0)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups = old_groups[1:]
    assert sorted(old_groups) == sorted(new_groups)


