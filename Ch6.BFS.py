#너비우선탐색 BFS알고리즘으로 친구혹은 친구의 친구들중 m으로 끝나는 사람 빨리 찾기
from collections import deque #덱 사용하기
#인물에 따라 친구가 누가 있는지 사전으로 추가
g = {}
g['you'] = ['alice', 'bob', 'claire']
g['bob'] = ['anuj','peggy']
g['alice'] = ['peggy']
g['claire'] = ['tom', 'jonny']
g['tom'] = []
g['jonny'] = []
g['peggy'] = []
g['anuj'] = []
#이름의 마지막글자가 m으로 끝나는 사람을 판매자로 지정하는 함수
def person_is_seller(name):
  return name[-1] == 'm'

def search(name):
  d = deque()
  #name의 친구들 리스트를 덱에 추가
  d += g[name]
  
  searched = []
  #덱이 비어있을 때까지 반복
  while d:
    person = d.popleft()
    #이미 확인한 사람인지 확인
    if not person in searched:
      #person이 m으로 끝나는 사람이 맞으면 반환
      if person_is_seller(person):
        return person
      #아니면 친구의 친구들까지 덱에 추가
      else:        
        d += g[person]
        #확인한 사람들을 searched 리스트에 추가
        searched.append(person)
  #친구와 친구의 친구들중에 m으로 끝나는 사람이 없을 경우
  return False

print(search('you')) #tom이 출력된다.
