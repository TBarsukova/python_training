import random
import string

import pytest

from model.contact import Contact


def randstr(prefix, maxlen, letters=True, digits=True, punctuation=True, spaces=True):
    symbols = ""
    if letters:     symbols += string.ascii_letters
    if digits:      symbols += string.digits
    if punctuation: symbols += string.punctuation
    if spaces:      symbols += " "*10
    return prefix + "".join (random.choice(symbols) for _ in range(random.randrange(maxlen))).strip()

testdata = [Contact(first_name="", middle_name="", last_name="")] + [
        Contact(
            first_name=randstr("f_name_", 10, digits=False, punctuation=False),
            middle_name=randstr("m_name_", 10, digits=False, punctuation=False),
            last_name=randstr("l_name_", 10, digits=False, punctuation=False),
            nick_name=randstr("n_name_", 10, digits=False, punctuation=False),
            company=randstr("comp_", 10, digits=False, punctuation=False),
            title=randstr("title_", 10, digits=False, punctuation=False),
            address=randstr("addr_", 10, punctuation=False),
            home=randstr("tel_", 10, letters=False, punctuation=False),
            phone2=randstr("tel_", 10, letters=False, punctuation=False),
            mobile=randstr("tel_", 10, letters=False, punctuation=False),
            work=randstr("tel_", 10, letters=False, punctuation=False),
            fax=randstr("tel_", 10, letters=False, punctuation=False),
            email=randstr("mail@", 10, punctuation=False, spaces=False),
            email2=randstr("mail@", 10, punctuation=False, spaces=False),
            email3=randstr("mail@", 10, punctuation=False, spaces=False),
            www=randstr("mail@", 10, punctuation=False, spaces=False),
        ) for _ in range(5)
        ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts) == sorted(new_contacts)