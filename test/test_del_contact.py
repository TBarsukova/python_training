from model.contact import Contact

def test_delete_first_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(first_name="to_be_deleted"))
    app.contact.delete_contact(0)