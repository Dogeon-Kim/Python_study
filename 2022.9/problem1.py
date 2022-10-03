dans = (2, 3, 4, 5, 6, 7, 8, 9)

print('구구단표')
print('-' * 30)

for j in dans:
    for i in range(1, 10):
        print("%d x %d = %d" %(j, i, j*i))
    print("-" * 30)
