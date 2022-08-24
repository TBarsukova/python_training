from model.contact import Contact

    
def test_add_contact(app):
    contact = Contact(first_name="Hello", last_name="World")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts) == sorted(new_contacts)

def test_add_empty_contact(app):
    contact = Contact(first_name="", last_name="")
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts) == sorted(new_contacts)
