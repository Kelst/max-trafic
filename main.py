import tools
# import db
# # витягуємо дані із таблиць
# user_list=db.get_data_from_table("table_name")

test_data=[]
class MyObject:
    def __init__(self,uid, sent, recv, acct_input_gigawords, acct_output_gigawords, start):
        self.sent = sent
        self.recv = recv
        self.acct_input_gigawords = acct_input_gigawords
        self.acct_output_gigawords = acct_output_gigawords
        self.start = start
        self.uid=uid


test_data.append(MyObject("1","957618465","3534234902","0","3","2023-04-21 11:08:59"))
test_data.append(MyObject("1","961924849","3359788091","0","0","2023-04-20 11:28:56"))
test_data.append(MyObject("1","287039191","1004552597","0","2","2023-04-19 12:42:25"))
test_data.append(MyObject("2","122792","140654","0","0","2023-01-19 12:40:40"))

elements = [
    {"uid": 1, "start": "2023-04-27", "sent": 10, "recv": 20, "acct_input_gigawords": 30, "acct_output_gigawords": 40},
    {"uid": 2, "start": "2023-04-27", "sent": 11, "recv": 21, "acct_input_gigawords": 31, "acct_output_gigawords": 41},
    {"uid": 1, "start": "2023-04-26", "sent": 12, "recv": 22, "acct_input_gigawords": 32, "acct_output_gigawords": 42},
    {"uid": 2, "start": "2023-04-26", "sent": 13, "recv": 23, "acct_input_gigawords": 33, "acct_output_gigawords": 43},
    {"uid": 3, "start": "2023-04-27", "sent": 14, "recv": 24, "acct_input_gigawords": 34, "acct_output_gigawords": 44},
]


print(tools.group_by_uid(elements))