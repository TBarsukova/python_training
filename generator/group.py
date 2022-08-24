import getopt
import sys

from model.group import Group
from .common import randstr, write_json, process_opts

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError:
    getopt.usage()
    sys.exit(2)

n, f = process_opts(n=5, f="data/group.json", opts=opts)

testdata = [Group(name="", header="", footer="")] + [
    Group(
        name=randstr("name_", 10, punctuation=False), 
        header=randstr("header_", 20, punctuation=False), 
        footer=randstr("footer_", 20, punctuation=False)
        ) for _ in range(n)
    ]

write_json(path=f, testdata=testdata)