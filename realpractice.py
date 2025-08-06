from random import *
"""print(random()*10)
int를 써주면 정수형으로 변환
print(randrange(1,46))
print(randint(1,45))
x=randint(4,28)
print("오프라인 스터디 모임 날짜는 매월",str(x),"일로 선정되었습니다.")"""

print("내가 먹고싶은건", 1, "햄버거")
python='python is amazing'
print(python.lower())
index=python.index('n')
index=python.index('n', index+1)
print(index)
#find는 문자열 없으면 -1반환

#index는 오류변환 
"""1. 내장 함수 (Built-in Function)
파이썬이 전역적으로 제공하는 함수

어떤 자료형이든 적용 가능한 경우가 많음

형식: 함수이름(데이터)

예: len(), type(), sorted()"""

# %d<-정수형 <<""안에 %d를 넣고 "를 마치고 %d 값을 %뒤에 넣으면 대입됨
# %s<-문자열
#방법 2 {0 or 변수 }{1 or 변수}를 넣고 .format({0 or 변수},{1})<format 안에 있는 값 대입
#방법 3
#변수 설정> age=20, print(f"나의 나이는 {age}살입니다")

#print("백문이 불여일견, 백견이 불여일타")

print("저는"'류영광'"입니다.")
#\"\':문장 내에서 따옴표
print("저는\'류영광\'입니다.")
#\n 줄바꿈
#\\ :문장 내에서 따옴표
# \r:커서를 맨앞으로 가져옴
print("good girl\rbad")
# \t:탭키

#사이트별로 비밀번호를 만들어주는 프로그램 작성
a="http://naver.com"
a=a[a.index("//")+2:]
a=a[:a.index('.')]
print(a[:3]+str(len(a))+str(a.count('e'))+'!')


character=["류",'영','광']
print(character.insert(0,'앙'))


"""list=[4,4,2,3,1]
#정렬
list.sort()
print(list)
#뒤집
list.reverse()
print(list)"""

#모두 지우기, clear
# 다양한 자료형 안에 쓸 수 있음

#확장<extend, append랑 비슷

###사전
#키와 밸류(값)으로 이루어짐

"""📌 1. 키(key)와 값(value) 직관적으로 이해하기
비유
딕셔너리는 전화번호부랑 똑같아요.

Key → 사람 이름 (고유 식별자)

Value → 전화번호 (이름에 해당하는 정보)


phone_book = {
    "철수": "010-1111-1111",
    "영희": "010-2222-2222"
}
"철수" → Key

"010-1111-1111" → Value

📌 2. 키와 값의 특징
키(key)
고유해야 함 (중복 불가)

변경 불가능(Immutable) 자료형만 가능 → str, int, tuple 가능 / list 불가능


복사
편집
my_dict = {1: "하나", "이": 2, (1,2): "튜플 키"}
값(value)
중복 가능

어떤 자료형이든 가능 (list, dict, int, str, … 전부 가능)

📌 3. 자주 쓰는 딕셔너리 사용 패턴
① 값 꺼내기


person = {"name": "Tom", "age": 25}
print(person["name"])  # Tom
② 값 변경


person["age"] = 26
③ 새 항목 추가

person["job"] = "Developer"
④ 값 삭제

del person["job"]
⑤ 안전하게 값 꺼내기 (.get())

print(person.get("city", "정보 없음"))  # city 키 없으면 '정보 없음'
⑥ 모든 키, 값, 키-값 쌍 확인

print(person.keys())   # dict_keys(['name', 'age'])
print(person.values()) # dict_values(['Tom', 26])
print(person.items())  # dict_items([('name', 'Tom'), ('age', 26)])"""

cabinet = {3:"류영광", "영광":"류광"}
print(cabinet["영광"]) #주의 ""안에 들어갈 값은 무조건 키값
#변수.get()을 했을 땐 키값이 있으면 그 값 출력 없으면 NONE
#추가로 get(키, 밸류) 식으로 키값이 있으면 그 키값의 밸류를 출력, 없으면 키와 그에 밸류 반환
cabinet.get(5, "사용불가")
print(cabinet)
cabinet["영광"]="류영"
print(cabinet)
cabinet["oho"]="류류"
print(cabinet)

del cabinet["oho"]
print(cabinet)
print(cabinet.keys())# 키만 출력 ?dict_keys([이건 뭐지?])
print(cabinet.values()) #밸류만 출력
print(cabinet.items()) #키 밸류 쌍으로 출력

cabinet.clear()
print(cabinet)

#튜플
menu= ("치킨","돈까스")
print(menu[0])
#menu.add("생선가스")<-사용불가능, 튜플에선 사용 x
#값을 한번에 지정?
(name, age, hobby) = ("뭐시기","뭐시기","뭐시기")
print(name, age, hobby)

#집합(set)
#중복 안됨, 순서 없음
a={1,2,2,3,4,4,0}
print(a)
java={"유재석","김태호","하하"}
python=set(["유재석","김태호"]) #이런식으로도 만들 수 있음
#교집합
print(java & python)
print(java.intersection(python))
#합집합
print(java | python)
print(java.union(python))
#차집합
print(java - python)
print(java.difference(python))
#값 추가
java.add("김종국")
print(java)

#자료 구조 변경
menu={"커피","우유","주스"}
print(menu, type(menu))

a=range(1,21) #-range(1,21) #중복 안되니까 리스트니까 없애면 되겠구나
a=list(a)
shuffle(a)
winners=sample(a,4)
print("치킨 당첨자:{0}".format(winners[0]))
print("커피 당첨자:{0}".format(winners[1:]))