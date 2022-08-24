from model.group import Group

def test_add_group(app):
    group = Group(name="qwer", header="qwert", footer="qwerty")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups) == sorted(new_groups)