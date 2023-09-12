# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.group.update_first(Group(name="999999", header="999", footer="999"))

def test_edit_first_group_name(app):
    app.group.update_first(Group(name="888888"))
