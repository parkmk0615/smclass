import oracledb

# oracle 연결 -sql developer연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
# 연결 확인
print(conn.version)

# sql 실행창 오픈
# # 1개 검색된 데이터 호출 ##
# cursor=conn.cursor()
# sql="select count(*) from member"
# cursor.execute(sql)
# count1=cursor.fetchone()
# print("갯수: ",count1)

# #여러개데이터 검색된 데이터 호출 ##
cursor=conn.cursor()
sql="select * from member"
cursor.execute(sql)
rows=cursor.fetchall()
#print("갯수: ",rows)


# for row in rows:
#   print(row)
# print(rows[0][0],rows[0][1],rows[0][2])

for row in rows:
  print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}\t{row[6]}\t{row[7]}")

conn.close()





