# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    group = Group(name="123456", header="124", footer="235")
    old_groups = app.group.getAll()

    app.group.create(group)

    new_groups = app.group.getAll()
    assert len(old_groups) + 1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    group = Group(name="", header="", footer="")
    old_groups = app.group.getAll()

    app.group.create(group)

    new_groups = app.group.getAll()
    assert len(old_groups) + 1 == len(new_groups)

    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
