def test_add_group(app, db, json_group, check_ui):
    group = json_group
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups) == sorted(new_groups)
    if check_ui:
        assert sorted(new_groups) == sorted(app.group.get_group_list())