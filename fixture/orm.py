# -*- coding: utf-8 -*-
from datetime import datetime
from pony.orm import *
from pymysql.converters import decoders
from model.contact import Contact
from model.group import Group


class ORMFixture:
    db = Database()

    def __init__(self, host, port, database, user, password):
        self.db.bind("mysql", host=host, port=port, database=database, user=user, password=password)#, conv=decoders)
        self.db.generate_mapping()
        #sql_debug(True)

    def destroy(self):
        self.db.disconnect()

    class ORMGroup(db.Entity):
        _table_ = "group_list"
        id      = PrimaryKey(int,   column="group_id")
        name    = Optional(str,     column="group_name")
        header  = Optional(str,     column="group_header")
        footer  = Optional(str,     column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = "addressbook"
        id          = PrimaryKey(int,    column="id")
        firstname   = Optional(str,      column="firstname")
        lastname    = Optional(str,      column="lastname")
        address     = Optional(str,      column="address")
        home        = Optional(str,      column="home")
        mobile      = Optional(str,      column="mobile")
        work        = Optional(str,      column="work")
        phone2      = Optional(str,      column="phone2")
        email       = Optional(str,      column="email")
        email2      = Optional(str,      column="email2")
        email3      = Optional(str,      column="email3")
        deprecated  = Optional(datetime, column="deprecated") #if using conv=decoders then type should be =str, for the pony default use =datetime
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts, autoaggregation=False):
        def convert(contact):
            new_contact = Contact(
                id=str(contact.id),
                firstname=contact.firstname if not contact.firstname == "" else None,
                lastname=contact.lastname if not contact.lastname == "" else None,
                address=contact.address if not contact.address == "" else None,
                home=contact.home if not contact.home == "" else None,
                mobile=contact.mobile if not contact.mobile == "" else None,
                work=contact.work if not contact.work == "" else None,
                phone2=contact.phone2 if not contact.phone2 == "" else None,
                email=contact.email if not contact.email == "" else None,
                email2=contact.email2 if not contact.email2 == "" else None,
                email3=contact.email3 if not contact.email3 == "" else None
            )
            if autoaggregation:
                new_contact.set_all_phones()
                new_contact.set_all_emails()
            return new_contact

        return list(map(convert, contacts))

    def get_orm_group_by_id(self, group_id):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group_id))[0]
        return orm_group

    @db_session
    def get_group_by_id(self, group_id):
        return self.convert_groups_to_model(select(group for group in ORMFixture.ORMGroup if group.id == group_id))

    @db_session
    def get_contact_by_id(self, contact_id):
        return self.convert_contacts_to_model(select(contact for contact in ORMFixture.ORMContact if contact.id == contact_id))

    @db_session
    def get_all_groups(self):
        return self.convert_groups_to_model(select(group for group in ORMFixture.ORMGroup))

    @db_session
    def get_all_contacts(self, autoaggregation=False):
        return self.convert_contacts_to_model(select(contact for contact in ORMFixture.ORMContact if contact.deprecated is None), autoaggregation)

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = self.get_orm_group_by_id(group.id)
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.get_orm_group_by_id(group.id)
        return self.convert_contacts_to_model(
            select(contact for contact in ORMFixture.ORMContact if contact.deprecated is None and orm_group not in contact.groups)
        )

    @db_session
    def get_contact_ids_in_groups(self):
        return self.db.select("SELECT ag.id, ag.group_id FROM group_list AS gl INNER JOIN address_in_groups AS ag ON gl.group_id=ag.group_id LIMIT 100")

    @db_session
    def get_not_empty_groups(self):
        groups_id = self.db.select("SELECT DISTINCT ag.group_id FROM group_list AS gl INNER JOIN address_in_groups AS ag ON gl.group_id=ag.group_id LIMIT 100")
        return self.convert_groups_to_model(select(group for group in ORMFixture.ORMGroup if group.id in groups_id))
