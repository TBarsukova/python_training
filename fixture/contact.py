import re

from selenium.webdriver.support.ui import Select

from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        if not wd.find_elements_by_name("searchstring"):
            wd.find_element_by_link_text("home").click()

    def refresh_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()    

    def open_contact_edit_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()   
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()

    def open_contact_view_page(self, index):
        wd = self.app.wd
        self.open_contacts_page()   
        wd.find_elements_by_xpath("//img[@title='Details']")[index].click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init_contact_creation
        wd.find_element_by_link_text("add new").click()
        # fill_contact_form
        self.fill_contact_form(contact)
        # submit_contact_creation
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def select_contact(self, index=0, id=None):
        wd = self.app.wd
        if id is not None:
            wd.find_element_by_xpath(f"//input[@value={id}]").click()
        else:
            wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact(self, index=0, id=None):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact(index, id)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        self.refresh_contacts_page()
        self.contact_cache = None

    def modify_contact(self, index, data:Contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.open_contact_edit_page(index)
        # fill contacts form
        self.fill_contact_form(data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def fill_contact_form(self, contact:Contact):
        self.fill_form_field("firstname", contact.first_name)
        self.fill_form_field("middlename", contact.middle_name)
        self.fill_form_field("lastname", contact.last_name)
        self.fill_form_field("nickname", contact.nick_name)
        self.fill_form_field("company", contact.company)
        self.fill_form_field("title", contact.title)
        self.fill_form_field("address", contact.address)
        self.fill_form_field("home", contact.home)
        self.fill_form_field("mobile", contact.mobile)
        self.fill_form_field("work", contact.work)
        self.fill_form_field("fax", contact.fax)
        self.fill_form_field("phone2", contact.phone2)
        self.fill_form_field("email", contact.email)
        self.fill_form_field("email2", contact.email2)
        self.fill_form_field("email3", contact.email3)
        self.fill_form_field("homepage", contact.www)

    def fill_form_field(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)     

    def get_form_field(self, field_name):
        wd = self.app.wd
        return wd.find_element_by_name(field_name).get_attribute("value") or None

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name('entry'))

    contact_cache = None

    def get_contact_list(self, group=None):
        self.open_contacts_page()
        if group is not None:
            self.select_contact_group(group)
            self.contact_cache = None
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                cols = element.find_elements_by_tag_name('td')
                contact = Contact(
                    id=cols[0].find_element_by_tag_name("input").get_attribute("value"),
                    last_name=cols[1].text or None,
                    first_name=cols[2].text or None,
                    address=cols[3].text or None,
                    all_phones = cols[5].text or None,
                    all_emails = cols[4].text or None,
                    )
                self.contact_cache.append(contact)
        return self.contact_cache

    def get_contact_from_edit_page(self, index):
        self.open_contact_edit_page(index)
        contact = Contact(
            id=self.get_form_field("id"),
            first_name=self.get_form_field("firstname"),
            middle_name=self.get_form_field("middlename"),
            last_name=self.get_form_field("lastname"),
            nick_name=self.get_form_field("nickname"),
            company=self.get_form_field("company"),
            title=self.get_form_field("title"),
            address=self.get_form_field("address"),
            home=self.get_form_field("home"),
            phone2=self.get_form_field("phone2"),
            mobile=self.get_form_field("mobile"),
            work=self.get_form_field("work"),
            fax=self.get_form_field("fax"),
            email=self.get_form_field("email"),
            email2=self.get_form_field("email2"),
            email3=self.get_form_field("email3"),
            www=self.get_form_field("homepage")
        )
        return contact

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page(index)
        content = wd.find_element_by_id('content')

        # Parse all phones
        if len(content.text.split("\n\n")) > 1:
            all_phones = content.text.split("\n\n")[1]
            all_phones = re.sub(r"H: ", "", all_phones)
            all_phones = re.sub(r"M: ", "", all_phones)
            all_phones = re.sub(r"W: ", "", all_phones)
            all_phones = re.sub(r"F:.*", "", all_phones)
            all_phones = re.sub(r"\n$", "", all_phones)
        else:
            all_phones = ""
        if len(content.text.split("\n\n\n")) > 1:
            secondary_block = content.text.split("\n\n\n")[1]
            phone2 = re.search(r"P: (.+)", secondary_block)
            if phone2 is not None:
                all_phones = "\n".join([all_phones, phone2.group(1)])

        # Parse all emails
        all_emails = content.find_elements_by_tag_name("a")
        all_emails = filter(lambda x: x.get_attribute("href").startswith("mailto"), all_emails)
        all_emails = [x.text for x in all_emails]
        all_emails = "\n".join(all_emails)

        contact = Contact(
            id=self.get_form_field("id"),
            all_phones=all_phones or None,
            all_emails=all_emails or None,
            )
        return contact

    def add_to_group(self, contacts:list, group):
        wd = self.app.wd
        self.open_contacts_page()
        for contact in contacts:
            self.select_contact(id=contact.id)
        dropdown = wd.find_element_by_name("to_group")
        dropdown.click()
        Select(dropdown).select_by_value(group.id)
        wd.find_element_by_name("add").click()
        self.refresh_contacts_page()

    def remove_from_group(self, contacts:list, group):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_group(group)
        for contact in contacts:
            self.select_contact(id=contact.id)
        wd.find_element_by_name("remove").click()
        self.refresh_contacts_page()

    def select_contact_group(self, group):
        wd = self.app.wd
        dropdown = wd.find_element_by_name("group")
        dropdown.click()
        Select(dropdown).select_by_value(group.id)
