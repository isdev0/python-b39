# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, orm, data_groups):
    old_groups = orm.get_all_groups()
    app.group.create(data_groups)
    new_groups = orm.get_all_groups()
    old_groups.append(data_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
