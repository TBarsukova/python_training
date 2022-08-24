from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()

    def select_group(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_group(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()

    def modify_group(self, index, data:Group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill form
        self.fill_group_form(data)
        # submit modification
        wd.find_element_by_name("update").click()

    def fill_group_form(self, group:Group):
        self.fill_form_field("group_name", group.name)
        self.fill_form_field("group_header", group.header)
        self.fill_form_field("group_footer", group.footer)

    def fill_form_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
