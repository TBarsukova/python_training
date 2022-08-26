from model.contact import Contact
from random import choice
    
def test_modify_random_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    if not old_contacts:
        app.contact.create(Contact(first_name="to_be_deleted"))
        old_contacts = db.get_contact_list()
    contact = choice(old_contacts)
    contact.first_name="modified_name"
    contact.last_name="modified_surname"
    app.contact.modify_contact(contact)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts) == sorted(new_contacts)
    if check_ui:
        assert sorted(new_contacts) == sorted(app.contact.get_contact_list())