# -*- coding: utf-8 -*-
from model.group import Group
import allure


def test_add_group(app, db, data_groups):
    with allure.step("Given a group list"):
        old_groups = db.get_all_groups()

    with allure.step("When I add the group %s to the list" % data_groups):
        app.group.create(data_groups)

    with allure.step("Then the new group list is equal to the old list with the added group"):
        new_groups = db.get_all_groups()
        old_groups.append(data_groups)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
