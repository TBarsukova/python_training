from fixture.orm import ORMFixture

db = ORMFixture(
    host="127.0.0.1", 
    name="addressbook", 
    user="root", 
    password="")

for item in db.get_contact_list():
    print(item)
