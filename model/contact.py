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

    def __eq__(self, other):
        return all([
            any([
                self.id == other.id,
                self.id is None,
                other.id is None,
            ]),
            any([
                self.first_name == other.first_name,
                self.first_name == "" and other.first_name is None,
                self.first_name is None and other.first_name == "",
            ]),
            any([
                self.middle_name == other.middle_name,
                self.middle_name == "" and other.middle_name is None,
                self.middle_name is None and other.middle_name == "",
            ]),
            any([
                self.last_name == other.last_name,
                self.last_name == "" and other.last_name is None,
                self.last_name is None and other.last_name == "",
            ]),
            self.nick_name == other.nick_name,
            self.company == other.company,
            self.title == other.title,
            self.address == other.address,
            self.home == other.home,
            self.phone2 == other.phone2,
            self.mobile == other.mobile,
            self.work == other.work,
            self.fax == other.fax,
            self.email == other.email,
            self.email2 == other.email2,
            self.email3 == other.email3,
            self.www == other.www,
            self.all_phones == other.all_phones,
            self.all_emails == other.all_emails,
        ])

    def __repr__(self):
        return f"{self.id}:{self.first_name} {self.last_name}"

    def __gt__(self, other):
        if self.id is None:
            return True
        if other.id is None:
            return False

        return int(self.id) > int(other.id)