# -*- coding: utf-8 -*-
from model.group import Group
from timeit import timeit


def test_group_list(app, db):

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    # print("\n")
    # print(timeit(lambda: app.group.get_all(), number=1))
    # print(timeit(lambda: map(clean, db.get_all_groups()), number=1000))
    # assert False

    ui_list = app.group.get_all()
    db_list = map(clean, db.get_all_groups())

    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
