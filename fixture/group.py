from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.open_groups_page()
        self.group_cache = None

    def fill_group_form(self, group:Group):
        self.fill_form_field("group_name", group.name)
        self.fill_form_field("group_header", group.header)
        self.fill_form_field("group_footer", group.footer)

    def fill_form_field(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)    

    def select_group(self, index=0, id=None):
        wd = self.app.wd
        if id is not None:
            wd.find_element_by_xpath(f"//input[@value={id}]").click()
        else:
            wd.find_elements_by_name("selected[]")[index].click()

    def delete_group(self, index=0, id=None):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group(index, id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.open_groups_page()
        self.group_cache = None

    def modify_group(self, group:Group, index=None, id=None):
        wd = self.app.wd
        self.open_groups_page()
        if group.id:
            self.select_group(id=group.id)
        else:
            self.select_group(index, id)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill form
        self.fill_group_form(group)
        # submit modification
        wd.find_element_by_name("update").click()
        self.group_cache = None

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

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text or None
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
