from model.contact import Contact
from random import randrange
    
def test_modify_random_contact(app, db):
    if not app.contact.count():
        app.contact.create(Contact(first_name="to_be_deleted"))
    old_contacts = db.get_contact_list()
    contact = Contact(first_name="modified_name", last_name="modified_surname")
    index = randrange(len(old_contacts))   
    contact.id = old_contacts[index].id
    app.contact.modify_contact(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts) == sorted(new_contacts)