# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, json_groups):
    old_groups = app.group.get_all()
    app.group.create(json_groups)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_all()
    old_groups.append(json_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
