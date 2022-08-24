class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, 
                nick_name=None, title=None, company=None, address=None, 
                home=None, mobile=None, work=None, fax=None, 
                email=None, email2=None, email3=None, id=None, 
                all_emails=None, all_phones=None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.company = company
        self.title = title
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.id = id
        self.all_emails = all_emails
        self.all_phones = all_phones

    def __repr__(self):
        return f"{self.id}:{self.first_name} {self.last_name}"

    def __eq__(self, other):
        return None in [self.id, other.id] or self.id == other.id

    def __gt__(self, other):
        if self.id is None:
            return True
        if other.id is None:
            return False

        return int(self.id) > int(other.id)