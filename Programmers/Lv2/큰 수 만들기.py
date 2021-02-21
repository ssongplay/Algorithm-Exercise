# https://programmers.co.kr/learn/courses/30/lessons/42883
# 블로그 - https://velog.io/@ssongplay/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        # stack에 있는 값이 number의 가장 앞 숫자보다 작은 경우에
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # k값을 1 감소시키고
            k -= 1
            # stack에 있는 값을 제거해준 뒤
            stack.pop()
        # 새로운 값을 삽입해줌
        stack.append(num)
    # for문이 끝난 후에도 제거 횟수를 다 사용하지 않았으면 남은 횟수만큼 리스트 뒷부분 잘라줌    
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
