# -*- coding: utf-8 -*-
import random
from model.group import Group
from random import randrange


def test_delete_random_group(app, db, check_ui):
    if len(db.get_all_groups()) == 0:
        app.group.create(Group(name="5555"))

    old_groups = db.get_all_groups()
    group = random.choice(old_groups)

    # index = randrange(len(old_groups))
    # print("\nRandom Index: " + str(index))
    print("\nRandom Id: " + str(group.id))

    app.group.delete_by_id(group.id)

    new_groups = db.get_all_groups()
    assert len(old_groups) - 1 == len(new_groups)

    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui: assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_all(), key=Group.id_or_max)
