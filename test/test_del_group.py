# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_delete_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="5555"))

    old_groups = app.group.getAll()
    index = randrange(len(old_groups))
    print("\nRandom Index: " + str(index))
    app.group.delete_by_index(index)

    assert len(old_groups) - 1 == app.group.count()
    new_groups = app.group.getAll()

    old_groups[index:index+1] = []
    assert old_groups == new_groups
