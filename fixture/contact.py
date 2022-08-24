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

    def select_contact(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        self.refresh_contacts_page()
        self.contact_cache = None

    def modify_contact(self, index, data:Contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact(index)
        # open modification form
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
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
        self.fill_form_field("email", contact.email)
        self.fill_form_field("email2", contact.email2)
        self.fill_form_field("email3", contact.email3)

    def fill_form_field(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name('entry'))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                cols = element.find_elements_by_tag_name('td')
                contact = Contact(
                    last_name=cols[1].text,
                    first_name=cols[2].text,
                    address=cols[3].text,
                    all_emails=cols[4].text,
                    all_phones=cols[5].text,
                    id=cols[0].find_element_by_tag_name("input").get_attribute("value"),
                    )
                self.contact_cache.append(contact)
        return self.contact_cache
