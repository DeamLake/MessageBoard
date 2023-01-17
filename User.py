#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：main.py 
@File    ：User.py
@IDE     ：PyCharm 
@Author  ：DeamLake
@Date    ：2023/1/4 18:18 
"""

from enum import Enum


class User(object):
    def __init__(self, userID, password, name):
        self.userID = userID
        self.password = password
        self.name = name

    userIDPool = set()
    userNamePool = set()
    userList = {}

    class UserCheckEnum(Enum):
        FINE = 0
        ID_EXIST = 1
        NAME_EXIST = 2
        ID_NOT_EXIST = 3
        PASSWORD_WRONG = 4

    @staticmethod
    def checkLogIn(userID, userPassword):
        if userID not in User.userIDPool:
            return User.UserCheckEnum.ID_NOT_EXIST, None

        current_user = User.userList[userID]
        if current_user.password != userPassword:
            return User.UserCheckEnum.PASSWORD_WRONG, None

        return User.UserCheckEnum.FINE, current_user

    @staticmethod
    def checkLogOn(userID, userPassword, userName):
        if userID in User.userIDPool:
            return User.UserCheckEnum.ID_EXIST, None
        if userName in User.userNamePool:
            return User.UserCheckEnum.NAME_EXIST, None

        current_user = User(userID, userPassword, userName)
        User.userIDPool.add(userID)
        User.userNamePool.add(userName)
        User.userList[userID] = current_user
        return User.UserCheckEnum.FINE, current_user


