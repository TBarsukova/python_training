import random
import string

import pytest

from model.group import Group


def randstr(prefix, maxlen, letters=True, digits=True, punctuation=True, spaces=True):
    symbols = ""
    if letters:     symbols += string.ascii_letters
    if digits:      symbols += string.digits
    if punctuation: symbols += string.punctuation
    if spaces:      symbols += " "*10
    return prefix + "".join (random.choice(symbols) for _ in range(random.randrange(maxlen)))

testdata = [Group(name="", header="", footer="")] + [
    Group(
        name=randstr("name_", 10, punctuation=False), 
        header=randstr("header_", 20, punctuation=False), 
        footer=randstr("footer_", 20, punctuation=False)
        ) for _ in range(5)
    ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups) == sorted(new_groups)