t = 0
d = 0
for i in open('18-21.txt', encoding='UTF-8'):
    print(i, end='')
    t += 1
    for j in i:
        if j == 'ж':
            d += 1
print(end='\n')
print('Кол-во строк:   ', t, end='\n')
print('Кол-во букв "ж":   ', d, end='\n')

f3 = open('18-21.txt', encoding='UTF-8')
l = f3.readline()
l[0], l[3] = l[3], l[0]
f3.close()

f4 = open('18-21_2.txt', 'w')
f4.writelines(l)
f4.close()
