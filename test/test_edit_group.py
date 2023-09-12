# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first(Group(name="999999", header="999", footer="999"))
    app.session.logout()

def test_edit_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.update_first(Group(name="888888"))
    app.session.logout()
