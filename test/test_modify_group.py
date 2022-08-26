from model.group import Group
from random import choice
    
def test_modify_random_group_name(app, db, check_ui):
    old_groups = db.get_group_list()
    if not old_groups:
        app.group.create(Group(name="to_be_deleted"))
        old_groups = db.get_group_list()
    group = choice(old_groups)
    group.name = "modified name"
    app.group.modify_group(group)
    new_groups = db.get_group_list()
    assert sorted(old_groups) == sorted(new_groups)
    if check_ui:
        assert sorted(new_groups) == sorted(app.group.get_group_list())