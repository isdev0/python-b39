# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_first(app):
    if app.group.count() == 0:
        app.group.create(Group(name="5555"))
    app.group.delete_first()
