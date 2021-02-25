# 문제 - https://programmers.co.kr/learn/courses/30/lessons/12941
# 블로그 - https://velog.io/@ssongplay/프로그래머스-최솟값-만들기-Python

def solution(A,B):
    answer = 0
    A.sort(reverse = True)
    B.sort()
    for i in range(len(A)):
        answer += (A[i]*B[i])
    return answer
