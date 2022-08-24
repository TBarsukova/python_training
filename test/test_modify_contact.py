from model.contact import Contact

    
def test_modify_first_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(first_name="to_be_deleted"))
    app.contact.modify_contact(0, Contact(first_name="abc", last_name="def", address="ghk"))