# -*- coding: utf-8 -*-
import random
import string
from model.group import Group


constant = [
    Group(name="GroupName1", header="GroupHeader1", footer="GroupFooter1"),
    Group(name="GroupName2", header="GroupHeader2", footer="GroupFooter2")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name_", 10), header=random_string("header_", 20), footer=random_string("footer_",20))
    for i in range(5)
]
