# 이게 아닌가봐

def solution(s):
    answer = True
    s = list(s)
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True if s.count('(')==s.count(')') and s[0]==('(') and s[-1]==(')') else False
