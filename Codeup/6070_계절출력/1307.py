# 문제 이해
# -> 월이 입력될 때 계절 이름을 영어로 출력한다. 

# 문제 해결 계획
# -> 정수를 입력받고 if문을 써서 입력받은 정수에 따른 계절을 영어로 출력한다.  

# 사전 지식
# -> 12, 1, 2월 : 겨울 / 3, 4, 5월 : 봄 / 6, 7, 8월 : 여름 / 9, 10, 11월 : 가을 

# 코드

a = int(input())

if a == 12 or a == 1 or a == 2:
    print('winter')
elif a == 3 or a == 4 or a == 5:
    print('spring')
elif a == 6 or a == 7 or a == 8:
    print('summer')
else:
    print('fall')

# 문제를 풀면서 느낀 점 or 깨달은 점
# -> C언어에서는 or 연산을 "||" 로 하는데 파이썬에서는 "or" 로 해서 좀 더 직관적이고 편했다. 
