from model.group import Group

    
def test_modify_first_group_name(app):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))

    old_groups = app.group.get_group_list()
    group = Group(name="new_group_name")
    group.id = old_groups[0].id
    app.group.modify_group(0, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups) == sorted(new_groups)


