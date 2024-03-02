l = ['-1 -2 -3 -4 -5 -6 -7 -8']
f1 = open('data_1.txt', 'w')
f1.writelines(l)
f1.close()

f1 = open('data_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

f1 = open('data_1.txt')
f1 = open('data_1.txt', 'a')
f1.write('\n')
arf = sum(k) / len(k)
print('Кол-во элементов: ', len(k), 'Среднее арифметическое: ', arf, file = f1)
f1.close()

#_____________________________________________________________________________________________________________

a = ['1 2 3 4 5 6 7 8']
f2 = open('data_2.txt', 'w')
f2.writelines(a)
f2.close()

f2 = open('data_2.txt')
s = f2.read()
s = s.split()
for i in range(len(s)):
    s[i] = int(s[i])
f1.close()

f2 = open('data_2.txt')
f2 = open('data_2.txt', 'a')
f2.write('\n')
arf = sum(s) / len(s)
print('Кол-во элементов: ', len(s), 'Среднее арифметическое: ', arf, file = f2)
f2.close()