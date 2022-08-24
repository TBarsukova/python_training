from model.contact import Contact

    
def test_modify_first_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(first_name="to_be_deleted"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="modified_name", last_name="modified_surname")
    contact.id = old_contacts[0].id
    app.contact.modify_contact(0, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts) == sorted(new_contacts)