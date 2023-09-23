# -*- coding: utf-8 -*-
from datetime import datetime
from pony.orm import *
from pymysql.converters import decoders
from model.contact import Contact
from model.group import Group


class ORMFixture:
    db = Database()

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
        deprecated  = Optional(datetime, column="deprecated") #if using conv=decoders then type should be =str, for the pony default use =datetime
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, port, database, user, password):
        self.db.bind("mysql", host=host, port=port, database=database, user=user, password=password)#, conv=decoders)
        self.db.generate_mapping()
        #sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    def get_orm_group_by_id(self, group_id):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group_id))[0]
        return orm_group

    @db_session
    def get_group_by_id(self, group_id="199"):
        return self.convert_groups_to_model(select(group for group in ORMFixture.ORMGroup if group.id == group_id))

    @db_session
    def get_all_groups(self):
        return self.convert_groups_to_model(select(group for group in ORMFixture.ORMGroup))

    @db_session
    def get_all_contacts(self):
        return self.convert_contacts_to_model(select(contact for contact in ORMFixture.ORMContact if contact.deprecated is None))

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
