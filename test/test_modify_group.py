from model.group import Group

    
def test_modify_first_group_name(app):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))

    old_groups = app.group.get_group_list()
    group = Group(name="new_group_name")
    group.id = old_groups[0].id
    app.group.modify_group(0, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups) == sorted(new_groups)


def test_modify_first_group_header(app):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))

    old_groups = app.group.get_group_list()
    group = Group(header="new_group_header")
    group.id = old_groups[0].id
    app.group.modify_group(0, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups) == sorted(new_groups)

