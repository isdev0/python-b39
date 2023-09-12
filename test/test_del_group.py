# -*- coding: utf-8 -*-

def test_delete_first(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first()
    app.session.logout()