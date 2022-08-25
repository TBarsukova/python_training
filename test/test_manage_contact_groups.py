from random import choice, sample
from model.contact import Contact
from model.group import Group

def test_add_contact_to_group(app, orm):
    autopopulate(app, orm, 10)
    group = choice(orm.get_group_list())
    old_contacts_in_group = orm.get_contacts_in_group(group)
    contacts = sample(orm.get_contact_list(), k=5)
    app.contact.add_to_group(contacts, group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    for contact in contacts:
        if contact not in old_contacts_in_group:
            old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group) == sorted(new_contacts_in_group)


def test_remove_contact_from_group(app, orm):
    autopopulate(app, orm, 10)
    group = choice(orm.get_group_list())
    number_of_contacts = len(orm.get_contacts_in_group(group))
    if number_of_contacts < 5:
        contacts = sample(orm.get_contacts_not_in_group(group), k=5-number_of_contacts)
        app.contact.add_to_group(contacts, group)

    contacts = sample(orm.get_contacts_in_group(group), k=3)
    old_contacts_in_group = orm.get_contacts_in_group(group)
    app.contact.remove_from_group(contacts, group)
    new_contacts_in_group = orm.get_contacts_in_group(group)
    for contact in contacts:
        old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group) == sorted(new_contacts_in_group)
    # Тест проваливается, если у группы нет имени. Это баг в приложении addressbook.


def autopopulate(app, orm, min_contacts):
    # Add new contacts and new group
    number_of_contacts = len(orm.get_contact_list())
    if number_of_contacts < min_contacts:
        for i in range(min_contacts - number_of_contacts):
            app.contact.create(Contact(first_name=f"autopopulated_{i}"))
    if not orm.get_group_list():
        app.group.create(Group(name=f"autopopulated"))