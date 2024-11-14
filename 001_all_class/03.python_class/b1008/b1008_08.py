import copy
# 얕은 복사
score=[100,90,95]
name = ["홍길동","유관순","이순신",]

n=name
n[2] ="김구"

print(n)

print(name)

# 깊은 복사
name = ["홍길동","유관순","이순신",]
# n=name # 얕은복사/ 주소값이 n에 대입
n=name[:] # 깊은 복사/ "홍길동","유관순,"이순신"이 n에 대입


name =["홍길동","유관순","이순신"]
score = [100,90,95]

n_dic =dict(zip(name,score))
print(n_dic)

# a=n_dic # 얕은 복사
a=copy.deepcopy(n_dic)# 깊은 복사

a['홍길동'] = 0
print(a)
print(n_dic)