import sys
input = sys.stdin.readline  # 입력을 받는다.

n = int(input())  # 파일 개수 n을 입력받는다.

file = dict()  # 파일이라는 이름의 빈 딕셔너리를 만든다.
for _ in range(n):  # 입력받은 n 만큼 반복한다.
    extend = (input().split('.'))[1]  # 파일 이름을 '.'으로 나눠 확장자 부분을 extend에 저장한다.
    if not extend in file:  # 만약 확장자가 딕셔너리에 없으면
        file[extend] = 1  # 새로운 확장자를 1로 초기화시킨다.
    else:  # 이미 딕셔너리에 있는 확장자라면
        file[extend] += 1  # 확장자 수를 1증가 시킨다.

sort_file = sorted(file.items())  # 딕셔너리를 확장자 정렬한다.

for key, value in sort_file:  # 정렬된 딕셔너리의 키와 개수를 하나씩 꺼낸다.
    print(key.rstrip(), value)  # 줄바꿈 제거하고 개수를 출력한다.