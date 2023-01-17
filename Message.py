#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：main.py 
@File    ：Message.py
@IDE     ：PyCharm 
@Author  ：DeamLake
@Date    ：2023/1/4 18:18 
"""

from enum import Enum


class Message(object):
    def __init__(self, messageID, userID, content):
        self.messageID = messageID
        self.userID = userID
        self.content = content
        self.usersLike = set()

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

    @staticmethod
    def updateMessage(message, optCode, optUserID):
        if optCode == Message.MessageOptEnum.ADD_MSG:
            Message.messageList.append(message)
            Message.messageDic[message.messageID] = message
        elif optCode == Message.MessageOptEnum.DEL_MSG:
            Message.messageList.remove(message)
            del Message.messageDic[message.messageID]
        elif optCode == Message.MessageOptEnum.LIKE_MSG:
            message.usersLike.add(optUserID)
        elif optCode == Message.MessageOptEnum.UNLIKE_MSG:
            if optUserID in message.usersLike:
                message.usersLike.remove(optUserID)

        Message.messageList.sort(key=lambda msg: len(msg.usersLike), reverse=True)

    @staticmethod
    def getMessagesByPageNum(pageNum):
        if (pageNum - 1) * 10 > len(Message.messageList):
            return None
        left = 10 * (pageNum - 1)
        return Message.messageList[left:left+10]

