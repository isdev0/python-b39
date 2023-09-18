# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_edit_random_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="555555", header="555", footer="5555"))

    old_groups = app.group.getAll()
    index = randrange(len(old_groups))
    print("\nRandom Index: " + str(index))
    group = Group(name="999999", header="999", footer="999")
    group.id = old_groups[index].id

    app.group.update_by_index(index, group)

    assert len(old_groups) == app.group.count()
    new_groups = app.group.getAll()

    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    # testing interrupted session using .logout() method
    app.session.logout()

# def test_edit_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="555555", header="555", footer="5555"))
#
#     old_groups = app.group.getAll()
#     app.group.update_first(Group(name="888888"))
#     new_groups = app.group.getAll()
#     assert len(old_groups) == len(new_groups)
