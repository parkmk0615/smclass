member = [{"id":"aaa","pw":"1111","name":"홍길동","nicname":"길동스","address":"서울시","money":1000000000},
          {"id":"bbb","pw":"2222","name":"유관순","nicname":"관순스","address":"부산시","money":1000000},
          {"id":"ccc","pw":"3333","name":"이순신","nicname":"순신스","address":"경기도","money":1000000},
          {"id":"ddd","pw":"4444","name":"강감찬","nicname":"감찬스","address":"인천시","money":20000000},
          {"id":"admin","pw":"5555","name":"김구","nicname":"김스","address":"대구시","money":1000000}]
# member.txt 파일 생성해서 csv파일 형태로 저장

f=open('member.txt','w',encoding='utf-8')
for m in member:
  f.write(f"{m['id']},{m['pw']},{m['name']},{m['nicname']},{m['address']},{m['money']}\n")
  
f.close()


# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
#   {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
#   {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]

# #students 딕셔너리 파일을 메모장에 csv파일 형태로 저장하시오


# f= open('students.txt','w',encoding='utf-8')
# for i in students:
#   f.write(f"{i['no']},{i['name']},{i['eng']},{i['math']},{i['total']},{i['avg']},{i['rank']}\n")
  
# f.close()