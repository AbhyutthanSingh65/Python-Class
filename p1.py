"""a=1
for i in range(4):
    for j in range(i+1):
        if(i==j):
            break
        a=a*2
print(a//2)

a=[["A"for i in "bike"]for i in "car"]
print(a[2]*len([[2,3],[4,5]]))"""

"""a=1
for i in ["list","string"]:
    for j in "ij":
        a=a+3
    a=a-2
print([(i+2) for i in range(1,a,2)])"""

a = "education"
b = 123456
res = 0

for i in a:
    if i in ['a', 'e', 'i', 'o', 'u']:
        res = res + b % 10
        b = b // 10

b_str = str(b)
b1 = list(b_str)
while len(b1) < 3:
    b1.insert(0, '0')
   
digit = int(b1[2])
result = digit * b

print(result)
