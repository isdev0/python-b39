# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="555555", header="555", footer="5555"))

    old_groups = app.group.getAll()
    group = Group(name="999999", header="999", footer="999")
    group.id = old_groups[0].id

    app.group.update_first(group)

    new_groups = app.group.getAll()
    assert len(old_groups) == len(new_groups)

    old_groups[0] = group
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
