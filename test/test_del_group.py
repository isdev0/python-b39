# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first(app):
    if app.group.count() == 0:
        app.group.create(Group(name="5555"))
    old_groups = app.group.getAll()
    app.group.delete_first()
    new_groups = app.group.getAll()
    assert len(old_groups) - 1 == len(new_groups)
