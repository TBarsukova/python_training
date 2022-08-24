def test_add_contact(app, db, json_contact, check_ui):
    contact = json_contact
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts) == sorted(new_contacts)
    if check_ui:
        assert sorted(new_contacts) == sorted(app.contact.get_contact_list())