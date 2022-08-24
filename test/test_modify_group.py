from model.group import Group
from random import randrange
    
def test_modify_random_group_name(app):
    if not app.group.count():
        app.group.create(Group(name="to_be_deleted"))
    old_groups = app.group.get_group_list()
    group = Group(name="new_group_name")
    index = randrange(len(old_groups))  
    group.id = old_groups[index].id
    app.group.modify_group(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups) == sorted(new_groups)