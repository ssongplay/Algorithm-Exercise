# https://programmers.co.kr/learn/courses/30/lessons/12924
# 블로그 - https://velog.io/@ssongplay/프로그래머스-숫자의-표현Python

def solution(n):
    answer = 0
    for i in range(1, n):
        for j in range(i+1, n):
            i += j
            if i == n:
                answer += 1
                break
            if i > n:
                break
    return answer+1
    # 자기자신을 더해야하므로 answer+1 리턴
