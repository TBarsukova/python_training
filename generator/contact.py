import getopt
import sys

from model.contact import Contact
from .common import randstr, write_json, process_opts

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError:
    getopt.usage()
    sys.exit(2)

n, f = process_opts(n=5, f="data/contact.json", opts=opts)

testdata = [Contact(first_name="", middle_name="", last_name="")] + [
        Contact(
            first_name=randstr("f_name_", 10, digits=False, punctuation=False),
            middle_name=randstr("m_name_", 10, digits=False, punctuation=False),
            last_name=randstr("l_name_", 10, digits=False, punctuation=False),
            nick_name=randstr("n_name_", 10, digits=False, punctuation=False),
            company=randstr("comp_", 10, digits=False, punctuation=False),
            title=randstr("title_", 10, digits=False, punctuation=False),
            address=randstr("addr_", 10, punctuation=False),
            home=randstr("tel_", 10, letters=False, punctuation=False),
            phone2=randstr("tel_", 10, letters=False, punctuation=False),
            mobile=randstr("tel_", 10, letters=False, punctuation=False),
            work=randstr("tel_", 10, letters=False, punctuation=False),
            fax=randstr("tel_", 10, letters=False, punctuation=False),
            email=randstr("mail@", 10, punctuation=False, spaces=False),
            email2=randstr("mail@", 10, punctuation=False, spaces=False),
            email3=randstr("mail@", 10, punctuation=False, spaces=False),
            www=randstr("mail@", 10, punctuation=False, spaces=False),
        ) for _ in range(n)
        ]

write_json(path=f, testdata=testdata)