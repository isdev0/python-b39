# -*- coding: utf-8 -*-
import pymysql
from model.contact import Contact
from model.group import Group


class DbFixture:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=self.host, port=self.port, database=self.database, user=self.user, password=self.password, autocommit=True)

    def get_all_groups(self):
        sql_querry = "SELECT group_id, group_name, group_header, group_footer FROM group_list"
        cursor = self.connection.cursor()
        records = []
        try:
            cursor.execute(sql_querry)
            for row in cursor:
                (id, name, header, footer) = row
                records.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return records

    def get_all_contacts(self, autoaggregation=False):
        sql_querry = "SELECT id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 FROM addressbook WHERE deprecated='0000-00-00 00:00:00'"
        cursor = self.connection.cursor()
        records = []
        try:
            cursor.execute(sql_querry)
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                new_contact = Contact(
                    id=str(id),
                    firstname=firstname,
                    lastname=lastname,
                    address=address,
                    home=home,
                    mobile=mobile,
                    work=work,
                    phone2=phone2,
                    email=email,
                    email2=email2,
                    email3=email3
                )
                if autoaggregation:
                    new_contact.set_all_emails()
                    new_contact.set_all_phones()
                records.append(new_contact)
        finally:
            cursor.close()
        return records

    def destroy(self):
        self.connection.close()
