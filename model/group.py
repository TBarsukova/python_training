class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.name};{self.header};{self.footer}"

    def __eq__(self, other):
        return all([
            any([
                self.id == other.id,
                self.id is None,
                other.id is None,
            ]),
            any([
                self.name == other.name,
                self.name == "" and other.name is None,
                self.name is None and other.name == "",
            ]),
            any([
                self.header == other.header,
                self.header == "" and other.header is None,
                self.header is None and other.header == "",
            ]),
            any([
                self.footer == other.footer,
                self.footer == "" and other.footer is None,
                self.footer is None and other.footer == "",
            ]),
        ])

    def __gt__(self, other):
        if self.id is None:
            return True
        if other.id is None:
            return False

        return int(self.id) > int(other.id)
