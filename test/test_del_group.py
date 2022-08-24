from model.group import Group
from random import choice

def test_delete_random_group(app, db):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))
    old_groups = db.get_group_list()
    group = choice(old_groups)  
    app.group.delete_group(id=group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert sorted(old_groups) == sorted(new_groups)