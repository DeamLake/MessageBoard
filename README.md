# Easy MessageBoard by Python

Save data by file.

# Dependence

* Python 3.9
# Run

```powershell
python3 /path/to/PythonMessageBoard/message_board.py
login <username> <password> - 登录账号
logon <username> <password> <nickname> - 创建账号
logoff - 退出登录
list [n] - 查看留言版，n表示查看第几页。如果省略n显示第一页。
add_msg <content> - 增加留言
del_msg <msg_id> - 删除留言
like_msg <msg_id> - 点赞留言
unlike_msg <msg_id> - 取消点赞
q - 保存并退出系统
```


