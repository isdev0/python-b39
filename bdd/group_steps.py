from pytest_bdd import given, when, then
from model.group import Group


@given("a group list")
def group_list(db):
    return db.get_all_groups()


@given("a group with <name>, <header> and <footer>")
def new_group(app, name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when("I add the group to the list")
def add_new_group(app, new_group):
    app.group.create(new_group)


@then("the new group list is equal to the old list with the added group")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_all_groups()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)