from model.group import Group
from .common import randstr


testdata = [Group(name="", header="", footer="")] + [
    Group(
        name=randstr("name_", 10, punctuation=False), 
        header=randstr("header_", 20, punctuation=False), 
        footer=randstr("footer_", 20, punctuation=False)
        ) for _ in range(5)
    ]