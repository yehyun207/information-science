import sys
n = int(sys.stdin.readline()) 

stack = []

for _ in range(n):
    s = sys.stdin.readline().split()
    if s[0] == 'push': ## push가 입력된다면
        stack.append(s[1]) ## stack이라는 배열의[1]에 값을 입력하고고
    elif s[0] == 'pop' : ## 만약 pop이 입력된다면
        if len(stack) > 0: print(stack.pop()) ## stack의 길이가 0보다 크면 stack의 pop을 출력하고고
        else: print(-1) ## 길이가 0보다 작다면 -1을 출력한다.
    elif s[0] == 'size': ## 만약 size가 입력된다면
        print(len(stack)) ## stack의 크기를 출력하고고
    elif s[0] == 'empty': ## empty가 입력된다면
        if len(stack)==0 : print(1) ## stack의 크기가 0이면 1을 출력하고
        else: print(0) ## 아니라면 0을 출력한다.
    elif s[0] == 'top': ## top이 입력된다면
        if len(stack)>0: print(stack[-1]) ## 스택이 비어있지 않다면 최상단 정수를 출력하고
        else: print(-1) ## 아니라면 -1을 출력한다.
