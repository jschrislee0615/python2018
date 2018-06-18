import csv
f = open('사망교통사고.csv', 'rt', encoding='UTF8')
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
print('값이 작아서 분류하기 힘든 것들의 합 = m')
print(m)

git = []
for i in result:
    if i not in res:
        git.append(i)
    else: pass

print('git에다가 result에서 res를 제외한 원소 옮겨쓰기')
print(git)

r = []
for i in num:
    if i not in n:
        r.append(i)
    else: pass

print('r에다가 num에서 n을 제외한 원소 옮겨쓰기')
print(r)

git.append('기타')
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