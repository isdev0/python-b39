# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_edit_random_group(app, orm):
    if len(orm.get_all_groups()) == 0:
        app.group.create(Group(name="555555", header="555", footer="5555"))

    old_groups = orm.get_all_groups()
    old_group = random.choice(old_groups)

    print("\nRandom Id: " + str(old_group.id))
    new_group = Group(name="999999", header="999", footer="999")
    new_group.id = old_group.id

    app.group.update_by_id(old_group.id, new_group)

    new_groups = orm.get_all_groups()
    assert len(old_groups) == len(new_groups)

    old_groups = list(map(lambda x: x if x != old_group else new_group, old_groups))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    # testing interrupted session using .logout() method
    app.session.logout()

# def test_edit_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="555555", header="555", footer="5555"))
#
#     old_groups = app.group.get_all()
#     app.group.update_first(Group(name="888888"))
#     new_groups = app.group.get_all()
#     assert len(old_groups) == len(new_groups)
