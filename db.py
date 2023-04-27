# import pymysql


# def get_data_from_table( chunk_size=5000):
#     #  список користувачів
#     user_list=[]
#     conn = pymysql.connect(host='localhost', user='username', password='password', db='database_name')
   
#     cur = conn.cursor()
   
#     cur.execute(f"SELECT COUNT(*) FROM internet_log")
#     total_rows = cur.fetchone()[0]
#     for offset in range(0, total_rows, chunk_size):
       
#         cur.execute(f"SELECT * FROM internet_log LIMIT {chunk_size} OFFSET {offset}")
#         rows = cur.fetchall()
       
#         for row in rows:
#             user_list.extend(row)

#     cur.execute(f"SELECT COUNT(*) FROM internet_log")
#     total_rows = cur.fetchone()[0]
#     for offset in range(0, total_rows, chunk_size):
       
#         cur.execute(f"SELECT * FROM internet_log LIMIT {chunk_size} OFFSET {offset}")
#         rows = cur.fetchall()
       
#         for row in rows:
#             user_list.extend(row)

#     cur.close()
#     conn.close()
#     return user_list