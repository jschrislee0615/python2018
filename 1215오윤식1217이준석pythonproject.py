import csv
f = open('���������.csv', 'rt', encoding='UTF8')
data = csv.reader(f)
next(data)
data=list(data)
result = []
for row in data :
    result.append(row[16])
    result = list(set(result))
print(result)

num=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for row in data :
    for i in range(0,len(result)) :
        if result[i] == row[16]:
            num[i] += 1
print(num)

res = []
n = []
for i in range(0,len(result)) :
    if num[i] <= 41 :
        res.append(result[i])
        n.append(num[i])
m = 0
for i in range(0,len(res)) :
    m = m+n[i]

print(res)
print(n)
print('���� �۾Ƽ� �з��ϱ� ���� �͵��� �� = m')
print(m)

git = []
for i in result:
    if i not in res:
        git.append(i)
    else: pass

print('git���ٰ� result���� res�� ������ ���� �Űܾ���')
print(git)

r = []
for i in num:
    if i not in n:
        r.append(i)
    else: pass

print('r���ٰ� num���� n�� ������ ���� �Űܾ���')
print(r)

git.append('��Ÿ')
r.append(m)

print(git)
print(r)

import matplotlib.pyplot as plt
plt.figure(figsize = (8,5), dpi = 500)
plt.rc('font',family='Malgun Gothic')
plt.barh(range(len(git)), r, height = 0.6)
plt.yticks(range(len(git)), git)
plt.show()

plt.figure(figsize = (8,5), dpi = 500)
plt.rc('font',family='Malgun Gothic')
plt.barh(range(len(res)), n, height = 0.6)
plt.yticks(range(len(res)), res)
plt.show()