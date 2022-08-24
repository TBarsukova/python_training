class Contact:

    def __init__(self, id=None, first_name=None, middle_name=None, last_name=None, 
                nick_name=None, title=None, company=None, address=None, 
                home=None, phone2=None, mobile=None, work=None, fax=None, 
                email=None, email2=None, email3=None,  www=None,
                all_phones=None, all_emails=None):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.company = company
        self.title = title
        self.address = address
        self.home = home
        self.phone2 = phone2
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.www = www
        self.all_phones = all_phones
        self.all_emails = all_emails


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