temp = {
    '월':25.5,
    '화':28.3,
    '수':33.2,
    '목':32.1,
    '금':17.3,
    '토':35.3,
    '일':33.3
}

date = input()

for k in temp:
    if date == k:
        print(temp[k])