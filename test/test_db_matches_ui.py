def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = db.get_group_list()
    ui_list.sort()
    db_list.sort()
    for ui_group, db_group in zip(ui_list, db_list):
        assert ui_group.id == db_group.id
        assert ui_group.name == db_group.name