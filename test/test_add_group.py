# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups):
    old_groups = db.get_all_groups()
    app.group.create(json_groups)
    new_groups = db.get_all_groups()
    old_groups.append(json_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
