from model.contact import Contact

    
def test_add_contact(app):
    contact = Contact(first_name="Hello", last_name="World")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts) == sorted(new_contacts)