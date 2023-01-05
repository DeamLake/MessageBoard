#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：main.py 
@File    ：message.py
@IDE     ：PyCharm 
@Author  ：DeamLake
@Date    ：2023/1/4 18:18 
"""

from enum import Enum


class Message(object):
    def __init__(self, message_id, user_id, content):
        self._messageID = message_id
        self._userID = user_id
        self._content = content
        self._usersLike = set()

    messageIDAutoInc = 0
    messageList = []
    messageDic = {}

    @staticmethod
    def getNextID():
        Message.messageIDAutoInc += 1
        return str(Message.messageIDAutoInc)

    @staticmethod
    def getMessageByID(mid):
        if mid not in Message.messageDic:
            return None
        return Message.messageDic[mid]

    class MessageOptEnum(Enum):
        ADD_MSG = 1
        DEL_MSG = 2
        LIKE_MSG = 3
        UNLIKE_MSG = 4

    @property
    def messageID(self):
        return self._messageID

    @property
    def userID(self):
        return self._userID

    @property
    def content(self):
        return self._content

    @property
    def usersLike(self):
        return self._usersLike

    @staticmethod
    def updateMessage(message, opt_code, opt_user_id):
        if opt_code == Message.MessageOptEnum.ADD_MSG:
            Message.messageList.append(message)
            Message.messageDic[message.messageID] = message
        elif opt_code == Message.MessageOptEnum.DEL_MSG:
            Message.messageList.remove(message)
            del Message.messageDic[message.messageID]
        elif opt_code == Message.MessageOptEnum.LIKE_MSG:
            message.usersLike.add(opt_user_id)
        elif opt_code == Message.MessageOptEnum.UNLIKE_MSG:
            if opt_user_id in message.usersLike:
                message.usersLike.remove(opt_user_id)

        Message.messageList.sort(key=lambda msg: len(msg.usersLike), reverse=True)

    @staticmethod
    def getMessagesByPageNum(page_num):
        if (page_num - 1) * 10 > len(Message.messageList):
            return None
        left = 10 * (page_num - 1)
        return Message.messageList[left:left+10]

