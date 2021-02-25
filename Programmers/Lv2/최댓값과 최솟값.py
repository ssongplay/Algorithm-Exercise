# https://programmers.co.kr/learn/courses/30/lessons/12939
# 블로그 - https://velog.io/@ssongplay/프로그래머스-최댓값과-최솟값-Python

def solution(s):    
    a = list(map(int, s.split(" ")))    
    return str(min(a)) + " " + str(max(a))
