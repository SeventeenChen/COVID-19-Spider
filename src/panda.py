import pandas as pd
import os


# currentConfirmedCount	confirmedCount	suspectedCount	curedCount	deadCount	seriousCount	updateTime

data = pd.read_csv('DXYOverall.csv', encoding='utf-8')
date = data["updateTime"]
# # for i in range(len(date)-1):
# #     if date[i] == date[i+1]:
# #         data.drop(i, inplace=True)
# title = ['currentConfirmedCount','confirmedCount','suspectedCount','curedCount','deadCount','seriousCount','updateTime']
# res = []
# print(data[title[6]][142:143])
# m, n = data.shape
# print(m,n)
# for i in range(m):
#     for j in range(n-1):
#         res.append(data[title[j]][i:i+1])
#
# with open('txt.txt', 'w') as txt:
#     for i in res:
#         txt.write(str(i))
for i in date:
    for j in range(6):
        print(i)


# j = []
# with open('txt.txt', 'r') as txt:
#     for i in txt:
#         j.append(i.split('    ')[-1])
#
# with open('j.txt', 'w') as count:
#     for i in j:
#         count.write(str(i))





