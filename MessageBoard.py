#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：main.py 
@File    ：MessageBoard.py
@IDE     ：PyCharm 
@Author  ：DeamLake
@Date    ：2023/1/2 22:23 
"""

from User import User
from Message import Message
import Storage


class MessageBoard(object):
    def __init__(self):
        self._currentUser = None
        Storage.loadFromFile()
        pass

    def run(self):
        print("Welcome to MessageBoard - v0.1\n"
              "You can type q to save and exit\n"
              "type ? to see more operations supported")
        while True:
            msg = input().strip().split(" ")
            if msg[0].lower() == "q":
                break
            elif msg[0].lower() == "?":
                MessageBoard.printOperationSupported()
            elif msg[0].lower() == "login":
                self._doLogIn(msg)
            elif msg[0].lower() == "logon":
                self._doLogOn(msg)
            elif msg[0].lower() == "logoff":
                self._doLogOff(msg)
            elif msg[0].lower() == "list":
                self._doList(msg)
            elif msg[0].lower() == "add_msg":
                self._doAddMsg(msg)
            elif msg[0].lower() == "del_msg":
                self._doDelMsg(msg)
            elif msg[0].lower() == "like_msg":
                self._doLikeMsg(msg)
            elif msg[0].lower() == "unlike_msg":
                self._doUnLikeMsg(msg)
            elif msg[0].lower() != " ":
                print("Unsupported operation.")

        Storage.saveToFile(Message.messageIDAutoInc, Message.messageList, User.userList.values())
        pass

    def _doLogIn(self, msg):
        if len(msg) != 3:
            print("The operation length is wrong!")
            return

        if self._currentUser is not None:
            print("User {} is online, Please logoff first!".format(self._currentUser.name))
            return

        code_ret, user_ret = User.checkLogIn(msg[1], msg[2])
        if code_ret == User.UserCheckEnum.ID_NOT_EXIST:
            print("ID {} not exist!".format(msg[1]))
        elif code_ret == User.UserCheckEnum.PASSWORD_WRONG:
            print("Wrong password!")
        else:
            self._currentUser = user_ret
            print("User {} login!".format(user_ret.name))
        pass

    def _doLogOn(self, msg):
        if len(msg) != 4:
            print("The operation length is wrong!")
            return

        if self._currentUser is not None:
            print("User {} is online, Please logoff first!".format(self._currentUser.name))
            return

        code_ret, user_ret = User.checkLogOn(msg[1], msg[2], msg[3])
        if code_ret == User.UserCheckEnum.ID_EXIST:
            print("ID {} exist!".format(msg[1]))
        elif code_ret == User.UserCheckEnum.NAME_EXIST:
            print("Name {} exist!".format(msg[3]))
        else:
            self._currentUser = user_ret
            print("New user {} login!".format(msg[3]))
        pass

    def _doLogOff(self, msg):
        if len(msg) != 1:
            print("The operation length is wrong!")
            return

        print("User {} logoff!".format(self._currentUser.name))
        self._currentUser = None
        pass

    def _doList(self, msg):
        if len(msg) > 2:
            print("The operation length is wrong!")
            return

        if len(msg) == 2 and ("[" not in msg[1] or "]" not in msg[1]):
            print("List format error!")
            return

        page_num = 1
        if len(msg) == 2 and msg[1][1:-1] != "":
            page_num = int(msg[1][1:-1])

        message_list = Message.getMessagesByPageNum(page_num)

        if message_list is None:
            print("Dont have so many messages!")
            return

        print("{:<{}} {:^{}} {:^{}} {:^{}} {:<{}}".format("message_id", 12, "user_id", 20, "if_you_like", 12,
                                                          "like_count", 12, "content", 20))
        for item in message_list:
            print("{:<{}} ".format(item.messageID, 12), end="")

            if self._currentUser is not None and self._currentUser.userID == item.userID:
                print("{:^{}} ".format("you", 20), end="")
            else:
                print("{:^{}} ".format(item.userID, 20), end="")

            if self._currentUser is not None and self._currentUser.userID in item.usersLike:
                print("{:^{}} ".format("✔", 12), end="")
            else:
                print("{:^{}} ".format(" ", 12), end="")

            print("{:^{}} ".format(len(item.usersLike), 12), end="")
            print("{}".format(item.content))
        pass

    def _doAddMsg(self, msg):
        if self._currentUser is None:
            print("Before you add message, You should login first!")
            return

        new_mid = Message.getNextID()
        new_message = Message(new_mid, self._currentUser.userID, ' '.join(msg[1:]))
        Message.updateMessage(new_message, Message.MessageOptEnum.ADD_MSG, self._currentUser.userID)
        pass

    def _doDelMsg(self, msg):
        if len(msg) != 2:
            print("The operation length is wrong!")
            return

        if self._currentUser is None:
            print("Before you del message, You should login first!")
            return

        message = Message.getMessageByID(msg[1])

        if message is None:
            print("Message {} does not Exist!".format(msg[1]))
            return

        if self._currentUser.userID != message.userID:
            print("It's not your message!")
            return

        Message.updateMessage(message, Message.MessageOptEnum.DEL_MSG, self._currentUser.userID)
        pass

    def _doLikeMsg(self, msg):
        if len(msg) != 2:
            print("The operation length is wrong!")
            return

        if self._currentUser is None:
            print("Before you like message, You should login first!")
            return

        message = Message.getMessageByID(msg[1])

        if message is None:
            print("Message {} does not Exist!".format(msg[1]))
            return

        Message.updateMessage(message, Message.MessageOptEnum.LIKE_MSG, self._currentUser.userID)
        pass

    def _doUnLikeMsg(self, msg):
        if len(msg) != 2:
            print("The operation length is wrong!")
            return

        if self._currentUser is None:
            print("Before you unlike message, You should login first!")
            return

        message = Message.getMessageByID(msg[1])

        if message is None:
            print("Message {} does not Exist!".format(msg[1]))
            return

        Message.updateMessage(message, Message.MessageOptEnum.UNLIKE_MSG, self._currentUser.userID)
        pass

    @staticmethod
    def printOperationSupported():
        print("login <username> <password> - 登录账号\n"
              "logon <username> <password> <nickname> - 创建账号\n"
              "logoff - 退出登录\n"
              "list [n] - 查看留言版，n表示查看第几页。如果省略n显示第一页。\n"
              "add_msg <content> - 增加留言\n"
              "del_msg <msg_id> - 删除留言\n"
              "like_msg <msg_id> - 点赞留言\n"
              "unlike_msg <msg_id> - 取消点赞\n"
              "q - 保存并退出系统")
        pass


if __name__ == "__main__":
    messageBoard = MessageBoard()
    messageBoard.run()
