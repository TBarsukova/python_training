from model.group import Group
from random import randrange

def test_delete_random_group(app):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))    
    app.group.delete_group(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.get_group_list()
    del old_groups[index]
    assert sorted(old_groups) == sorted(new_groups)