# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="555555", header="555", footer="5555"))

    app.group.update_first(Group(name="999999", header="999", footer="999"))

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="555555", header="555", footer="5555"))

    app.group.update_first(Group(name="888888"))
