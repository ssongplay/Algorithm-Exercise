# 문제 - https://programmers.co.kr/learn/courses/30/lessons/42885
# 블로그 - https://velog.io/@ssongplay/프로그래머스-구명보트-Python

def solution(people, limit):
    answer = len(people)
    people.sort()
    
    #가장 가벼운 사람과 무거운 사람을 같이 태워봄 
    small = 0  #처음 인덱스 
    big = len(people)-1  #마지막 인덱스
    
    while small < big :
        if people[small] + people[big] <= limit:
            small += 1
            answer -= 1
        big -= 1
                           
    return answer
