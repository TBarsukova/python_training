from model.contact import Contact
from random import choice
def test_delete_random_contact(app, db, check_ui):
    if not app.contact.count():
        app.contact.create(Contact(first_name="to_be_deleted"))
    old_contacts = db.get_contact_list()
    contact = choice(old_contacts)    
    app.contact.delete_contact(id=contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts) == sorted(new_contacts)
    if check_ui:
        assert sorted(new_contacts) == sorted(app.contact.get_contact_list())