from model.contact import Contact

def test_delete_first_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(first_name="to_be_deleted"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact(0)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts = old_contacts[1:]
    assert sorted(old_contacts) == sorted(new_contacts)