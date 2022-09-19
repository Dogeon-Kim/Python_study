# 문제 이해
# -> 월이 입력될 때 계절 이름을 출력한다. 

# 문제 해결 계획
# -> 
# 사전 지식
# -> 12,1,2 : winter  3,4,5 : spring  6,7,8 : summer  9,10,11 : fall
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

# 문제를 풀면서 느낀 점 || 깨달은 점

