# ds = 0
# db = 0
# d1 = []
# d2 = []
# with open('test.txt', 'r') as inf:
#     s = inf.readline()
#     for i in range(len(s)):
#         if s[i] < 'A':
#             ds = int(s[i])
#             d1.append(ds)
#             while s[i] < 'A':
#                 ds += int(s[i])
#             d1.append(ds)
#         elif s[i] >= 'A':
#             db = s[i]
#             d2.append(db)
# for i in range(len(d2)):
#     a = d1[i]
#     for j in range(a):
#         print(d2[i], end = "")

ds = ''
db = 0
d1 = []
d2 = []
s = 'a3b4c2e10b1'
i = 0
while i < len(s):
    if s[i] < 'A':
        i += 1
        while s[i] < 'A':
            ds += s[i-1]
            i += 1
        ds += s[i-1]
        d1.append(ds)
        ds = ''
    elif s[i] >= 'A':
        db = s[i]
        d2.append(db)
        i += 1
for i in range(len(d2)):
    a = d1[i]
    for j in range(a):
        print(d2[i], end = "")