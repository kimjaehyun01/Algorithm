#ch5 해시테이블
#투표 중복인원 확인하는 함수
voted = {}

def check_Vote(name):
  #voted 사전에 이름이 있으면
  if voted.get(name):
    print("돌려보내!")
  #없으면
  else:
    #voted 사전에 이름 추가
    voted[name] = True
    print("투표하세요")

check_Vote("mike")
check_Vote("mike")
check_Vote("mike")
