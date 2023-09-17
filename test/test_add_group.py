# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    old_groups = app.group.getAll()
    app.group.create(Group(name="123123", header="123", footer="234"))
    new_groups = app.group.getAll()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.getAll()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.getAll()
    assert len(old_groups) + 1 == len(new_groups)
