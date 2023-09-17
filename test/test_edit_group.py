# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="555555", header="555", footer="5555"))

    old_groups = app.group.getAll()
    app.group.update_first(Group(name="999999", header="999", footer="999"))
    new_groups = app.group.getAll()
    assert len(old_groups) == len(new_groups)

    # testing interrupted session using .logout() method
    app.session.logout()

def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="555555", header="555", footer="5555"))

    old_groups = app.group.getAll()
    app.group.update_first(Group(name="888888"))
    new_groups = app.group.getAll()
    assert len(old_groups) == len(new_groups)
