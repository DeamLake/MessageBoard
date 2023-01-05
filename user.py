#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：main.py 
@File    ：user.py
@IDE     ：PyCharm 
@Author  ：DeamLake
@Date    ：2023/1/4 18:18 
"""

from enum import Enum


class User(object):
    def __init__(self, user_id, password, name):
        self._userID = user_id
        self._password = password
        self._name = name

    userIDPool = set()
    userNamePool = set()
    userList = {}

    class UserCheckEnum(Enum):
        FINE = 0
        ID_EXIST = 1
        NAME_EXIST = 2
        ID_NOT_EXIST = 3
        PASSWORD_WRONG = 4

    @property
    def userID(self):
        return self._userID

    @property
    def password(self):
        return self._password

    @property
    def name(self):
        return self._name

    @staticmethod
    def checkLogIn(user_id, user_password):
        if user_id not in User.userIDPool:
            return User.UserCheckEnum.ID_NOT_EXIST, None

        current_user = User.userList[user_id]
        if current_user.password != user_password:
            return User.UserCheckEnum.PASSWORD_WRONG, None

        return User.UserCheckEnum.FINE, current_user

    @staticmethod
    def checkLogOn(user_id, user_password, user_name):
        if user_id in User.userIDPool:
            return User.UserCheckEnum.ID_EXIST, None
        if user_name in User.userNamePool:
            return User.UserCheckEnum.NAME_EXIST, None

        current_user = User(user_id, user_password, user_name)
        User.userIDPool.add(user_id)
        User.userNamePool.add(user_name)
        User.userList[user_id] = current_user
        return User.UserCheckEnum.FINE, current_user


