# -*- coding: utf-8 -*-
from sys import maxsize
import re


class Contact:

    def __init__(self,
                 id=None,
                 firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 title=None,
                 company=None,
                 address=None,
                 home=None,
                 mobile=None,
                 work=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 bday=None,
                 bmonth=None,
                 byear=None,
                 aday=None,
                 amonth=None,
                 ayear=None,
                 address2=None,
                 phone2=None,
                 notes=None,
                 all_phones=None,
                 all_emails=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones = all_phones
        self.all_emails = all_emails

    def phone_clear(self, phone):
        return re.sub("[() -]", "", phone)

    def merge_phones(self):
        return "\n".join(
            filter(lambda x: x != "",
                   map(lambda x: self.phone_clear(x),
                       filter(lambda x: x is not None, [self.home, self.mobile, self.work, self.phone2])
                       )
                   )
        )

    def merge_emails(self):
        return "\n".join(
            filter(lambda x: x != "",
                   filter(lambda x: x is not None, [self.email, self.email2, self.email3])
                   )
        )

    def set_all_phones(self):
        self.all_phones = self.merge_phones()

    def set_all_emails(self):
        self.all_emails = self.merge_emails()

    # representation redefinition
    def __repr__(self):
        return "%s:%s %s %s %s %s" % (self.id, self.firstname, self.lastname, self.address, self.all_phones, self.all_emails)

    # equality redefinition
    def __eq__(self, other):
        return (
                (self.id is None or other.id is None or self.id == other.id)
                and self.firstname == other.firstname
                and self.lastname == other.lastname
                and self.address == other.address
                and self.all_phones == other.all_phones
                and self.all_emails == other.all_emails
        )

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
