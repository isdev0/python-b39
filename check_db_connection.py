from fixture.db import DbFixture
from fixture.orm import ORMFixture

#db = DbFixture(host="localhost", port=3306, database="addressbook", user="root", password="")
db = ORMFixture(host="localhost", port=3306, database="addressbook", user="root", password="")

try:
    groups = db.get_all_groups()
    print("\n")
    for group in groups:
        print(group)
    print(len(groups))

    contacts = db.get_all_contacts()
    print("\n")
    for contact in contacts:
        print(contact)
    print(len(contacts))

finally:
    pass#db.destroy()
