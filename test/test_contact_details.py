from random import randrange
import re


def test_details_on_home_page_vs_edit_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = contacts[index]
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    contact_from_edit_page.all_phones = join_phones(contact_from_edit_page)
    contact_from_edit_page.all_emails = join_emails(contact_from_edit_page)
    assert contact_from_home_page.all_phones == contact_from_edit_page.all_phones
    assert contact_from_home_page.all_emails == contact_from_edit_page.all_emails
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.address == contact_from_edit_page.address

def test_details_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    for contact in contacts_from_db:
        contact.all_phones = join_phones(contact)
        contact.all_emails = join_emails(contact)
    for contact_from_db, contact_from_home_page in zip(sorted(contacts_from_db), sorted(contacts_from_home_page)):
        assert contact_from_home_page.all_phones == remove_double_spaces(contact_from_db.all_phones)
        assert contact_from_home_page.all_emails == contact_from_db.all_emails
        assert contact_from_home_page.last_name == remove_double_spaces(contact_from_db.last_name)
        assert contact_from_home_page.first_name == remove_double_spaces(contact_from_db.first_name)
        assert contact_from_home_page.address == remove_double_spaces(contact_from_db.address)

def test_details_on_view_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    contact_from_edit_page.all_phones = join_phones(contact_from_edit_page)
    contact_from_edit_page.all_emails = join_emails(contact_from_edit_page)
    assert clean(contact_from_view_page.all_phones) == contact_from_edit_page.all_phones
    assert clean(contact_from_view_page.all_emails) == contact_from_edit_page.all_emails


def clean(s):
    if s is not None:
        return re.sub(r"[() -]", "", s)

def remove_double_spaces(s):
    if s is not None:
        return re.sub(r"  ", " ", s)

def join_phones(contact):
    phones = [contact.home,  contact.mobile, contact.work, contact.phone2]
    phones = filter(lambda x: x is not None, phones)
    # Функция clean() и так callable, lambda не нужна. 
    # "" преобразуется в None при заполнении контакта в фикстуре.
    return "\n".join(map(clean, phones)) or None

def join_emails(contact):
    emails = [contact.email,  contact.email2, contact.email3]
    emails = filter(lambda x: x is not None, emails)
    return "\n".join(emails) or None