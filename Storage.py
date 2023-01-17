#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：main.py 
@File    ：Storage.py
@IDE     ：PyCharm 
@Author  ：DeamLake
@Date    ：2023/1/2 22:25 
"""

import os
from User import User
from Message import Message


def loadFromFile():
    if not os.path.exists("messageBoardData.txt"):
        return
    with open("messageBoardData.txt", "r", encoding="utf-8") as f:
        f.readline()
        Message.messageIDAutoInc = int(f.readline())

        f.readline()
        user_count = int(f.readline())
        for i in range(user_count):
            user_id, password, name = f.readline().strip().split(" ")
            new_user = User(user_id, password, name)
            User.userList[user_id] = new_user
            User.userIDPool.add(user_id)
            User.userNamePool.add(name)

        f.readline()
        message_count = int(f.readline())
        for i in range(message_count):
            message_id, user_id = f.readline().strip().split(" ")
            users_like = f.readline().strip().split(" ")
            content = f.readline().strip()
            new_message = Message(message_id, user_id, content)
            if users_like[0] != "":
                for u in users_like:
                    new_message.usersLike.add(u)
            Message.messageList.append(new_message)
            Message.messageDic[message_id] = new_message
    Message.messageList.sort(key=lambda msg: len(msg.usersLike), reverse=True)


def saveToFile(midInc, messageList, userList):
    with open("messageBoardDataTmp.txt", "w", encoding="utf-8") as f:
        f.write("# message ID inc\n")
        f.write("{}\n".format(midInc))
        f.write("# user list\n")
        f.write("{}\n".format(len(userList)))
        for item in userList:
            f.write("{} {} {}\n".format(item.userID, item.password, item.name))
        f.write("# message list\n")
        f.write("{}\n".format(len(messageList)))
        for item in messageList:
            f.write("{} {}\n".format(item.messageID, item.userID))
            for ul in item.usersLike:
                f.write("{} ".format(ul))
            f.write("\n")
            f.write("{}\n".format(item.content))
    if os.path.exists("messageBoardData.txt"):
        os.remove("messageBoardData.txt")
    os.rename("messageBoardDataTmp.txt", "messageBoardData.txt")




