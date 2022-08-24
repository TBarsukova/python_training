from sys import maxsize

from model.group import Group


def test_add_group(app):
    group = Group(name="qwer", header="qwert", footer="qwerty")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups) == sorted(new_groups)


def test_add_empty_group(app):
    group = Group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups) == sorted(new_groups)

