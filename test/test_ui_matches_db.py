# -*- coding: utf-8 -*-
from model.group import Group


def test_group_list(app, db):

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    ui_list = app.group.get_all()
    db_list = map(clean, db.get_all_groups())

    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
