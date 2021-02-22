# https://programmers.co.kr/learn/courses/30/lessons/12911?language=python3
# 블로그 - https://velog.io/@ssongplay/프로그래머스-다음-큰-숫자-Python
# 파이썬에서 진수 변환하기 - https://velog.io/@ssongplay/Python-진수-변환하기

def solution(n):
    i = n+1
    while 1:
        if list(bin(n)).count("1") == list(bin(i)).count("1"):
            return i
        else:
            i += 1
