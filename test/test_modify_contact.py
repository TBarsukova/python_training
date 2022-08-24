from model.contact import Contact

    
def test_modify_first_contact(app):
    app.open_home_page()
    app.contact.modify_contact(0, Contact(first_name="abc", last_name="def", address="ghk"))
    app.return_to_home_page()