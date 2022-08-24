from model.contact import Contact
from random import randrange

def test_delete_random_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(first_name="to_be_deleted"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))    
    app.contact.delete_contact(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    del old_contacts[index]
    assert sorted(old_contacts) == sorted(new_contacts)