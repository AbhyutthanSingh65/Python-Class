'''student=[]
marks=[]
for i in range(5):
    name=input("Enter name of the student{}".format(i+1))
    student.append(name)
    sum=0
    for j in range(3):
        mks=int(input("Enter mks of {} for sub {}".format(name,j+1)))
        sum+=mks
    perc=sum/30*100
    marks.append(perc)

i=0
for name in student:
    print(name,":-",marks[i])
    i+=1'''
'''teams=[] 
n=int(input("Enter no.of teams:"))
for i in range(n):
    t=input("Enter team name:".format(i+1))
    teams.append(t)
meet=int(input("Enter no. of meeting:"))
match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for k in range(meet):
            match.append([teams[i],teams[j]])
index=1
for i in match:
    print("Match{}: {} vs {}".format(match.index(i),i[0],i[1]))'''

'''a = [10,11,"Zakir","Bala",123,44,53,"Anuj",20,46,7,"Jack"]
a1=[]
a2=[]
a3=[]
for i in a:
    if(type(i)==str):
        a3.append(i)
    elif(i%2==1):
        a1.append(i)
    elif(i%2==0):
        a2.append(i)
    a1.sort()
    a2.sort()
    a3.sort()
print(a1+a2+a3)'''


'''notorious=["Darshan","Anuj","Rohit"]
names=["Anu","Darshan","Rohit","Jack","Priya","Bala","Rai","Ram","Raj","Ben"]
score=[2,5,6,8,3,5,6,9,8,2]
for i in range(len(names)):
    if score[i]>5:
        if names[i] not in notorious:
            print(names[i])'''


'''a = [23,129,45,200,45,34,27,77,88,127]
for i in a:
    if(i>50):
        a.remove(i)
print(sum(a)/len(a))'''


'''Boy=input("Enter a boy's name:")
Girl=input("Enter a girl's name:")
a1=list(Boy)
a2=list(Girl)
for i in range(len(a1)):
    for j in range(len(a2)):
        if(a1[i]==a2[j]):
            a1[i]='2'
            a2[j]='2'
for i in a1:
    if(i=='2'):
        a1.remove(i)
for i in a2:
    if(i=='2'):
        a2.remove(i)
num=len(a1)+len(a2)
print(num)


ans=['F','L','A','M','E','S']
index=0
while(len(ans)!=1):
    index=(index+(num-1))%len(ans)
    ans.pop(index)
print("The relation is",ans[0])'''

'''import random
name1=input("Enter player 1")
name2=input("Enter player 2")
print("Comp has fixed 5 nums in range of 1 to 10")
print("You guys have to guess it ... Ready?")
nums=[]
while len(nums)!=5:
    nums=random.randint(1,10)
    if num not in nums:
        nums.append(num)
num1=[]
num2=[]
s1=0
s2=0
for i in range(3):
    print("-----Round{}-----".format(i+1))
    print("Dear {} guess ur choice".format(name1))
    ch=int(input())
    if(ch in player1 or ch in player2):
        ch=int(input("It is already taken choose another"))'''


'''notes=[500,200,100,50,20,10,5,2,1]
amt=int(input("Enter the amount"))
cash=[]
for note in notes:
    while note<=amt:
        cash.append(note)
        amt-=note
print(cash)'''

'''ben="aaabbcccccaa"
c=1
res=""
for i in range(len(ben)):
    if i+1<len(ben) and ben[i]==ben[i+1]:
        c=c+1
    else:
        res=res+ben[i]+str(c)
        c=1
print(res)'''

'''a={1,2,3,4,5,6}
b={3,4,5,6,7,8,9}
print(a & b)
print(a-b)
print(b-a)
print(a^b)'''


'''stu={"name":"SACHIN","age":54,"runs":[543,245,490]}'''
'''stu["name"]="Raju"
print(stu)'''
'''for i in stu.keys():
    print(i)'''
'''print(stu["runs"][2])'''

'''student=[
    {"name": "Advik","marks":[30,50,54,67,90]}
]
print(student[0]["marks"][1])'''


'''students = [
    {"name": "raju", "dept": "cse", "marks": [20, 30, 40]},
    {"name": "vijay", "dept": "cse", "marks": [10, 70, 43]},
    {"name": "pavi", "dept": "ece", "marks": [22, 38, 56]},
    {"name": "rose", "dept": "ece", "marks": [26, 36, 89]},
    {"name": "virat", "dept": "ece", "marks": [16, 90, 43]}
]
for i in students:
    sum1=sum(i["marks"])
    per=sum1/3
    i["per"]=per
des=["First","Second","Third","Fourth"]
b=sorted(students,key=lambda x:x["per"], reverse=True)
index=1
for i in b:
    print("{}.{} is {} with {:.2f}".format(index+1,i["name"],des[index-1],i["per"]))
    index=index+1'''


'''from datetime import datetime
a=input("Enter first date(YYYY-MM-DD):")
b=input("Enter second date(YYYY-MM-DD):")
d1 = datetime.strptime(a,"%Y-%m-%d")
d2 = datetime.strptime(b,"%Y-%m-%d")
diff=d2-d1
print("Difference:",abs(diff.days),"days")'''

'''from datetime import datetime
import pytz
a='Asia/Tokyo'
tz=pytz.timezone(a)
b=datetime.now(tz)
print(b)'''

'''def ab(n):
    for i in range(20):
        if (i%n == 3):
            return
        else:
            print("Hai")
    print("Are you ok?")
ab(4)'''


'''def abc1():
    a=10
    b=20
    print(a+b)

def abc2(x,y):
    print(x+y)

def abc3():
    a=56
    b=89
    return a+b

def abc4(a,b):
    return a+b
abc1()
abc2(20,40)
res=abc3()
res=abc4(90,100)
print(res)'''


'''a=10
match a:
    case 10:
        print("Super")
    case 20:
        print("Excellent")
    case _:
        print("no")'''


'''while True:
    a = int(input("Enter a number (or 0 to exit): "))
    match a:
        case 10:
            print("Super")
        case 20:
            print("Excellent")
        case 0:
            print("Exiting...")
            break
        case _:
            print("no")'''

'''def circle():
      r=int(input("Enter radius of circle"))
      print("Area of circle is ",3.14*r*r)
def square(a):
      print("Area of square ",a*a)
def triangle():
    h = float(input("Enter the height of triangle: "))
    b = float(input("Enter the base of the triagle: "))
    return 0.5 * h * b
def rectangle(l, b):
    return l * b
while(True):
    print("1.CIRCLE")
    print("2.SQUARE")
    print("3.TRIANGLE")
    print("4.RECTANGLE")
    print("5.EXIT")
    ch=int(input("Enter your choice"))
    match ch:
        case 1:circle()
        case 2:
            a=int(input("Enter side of square"))
            square(a)
        case 3:
            res=triangle()
            print("Area of triangle is",res)
        case 4:
            a=int(input("Enter length of rect"))
            b=int(input("Enter breadth of rect"))
            res=rect(a,b)
            print("Area of rectangle is ",res)
        case 5:
              exit(0)
        case _:print("Invalid optins")'''


'''num=int(input("Enter any num"))
def gcd(a,b):
    while(b!=0):
        temp=a
        a=a%b
        a=b
        b=temp
    return a
def cop(a,b):
    return gcd(a,b==1)
for i in range(1,num):
    for j in range(1,i):
        for k in  range (1,j):
            if(j*j + k*k == i*i):
                print(k,j,i)'''


'''def prime(i):
    if(i==1):
        return False
    for j in range(2,i):
        if(i%j==0):
            return False
    return True
def sod(i):
    d=list(str(i))
    x=sum([int(i) for i in d])
    if (prime(x)):
        return True
    else:
        return False
def dig(i):
    while(i>0):
        d=i%10
        if(not prime(d)):
            return False
        i=i//10
    return True
for i in range(100,1000):
    if(prime(i) and sod(i) and dig(i)):
        print(i,end=" ") '''


'''def prime_f(n):
    if n==1:
        return
    i=2
    while(n%i!=0):
        i=i+1
    print(i,end=" ")
    prime_f(n // i)
n = int(input("Enter any number:"))
prime_f(n)'''


'''def print_board(board):
    for row in board:
        print(" ".join(row))
        print()
def safe(board,row,col,n):
    for i in range(row):
        if board[i][col]=='Q':
            return False
        
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n):
    if row == n:
        print_board(board)
        return

    for col in range(n):
        if safe(board, row, col, n):
            board[row][col] = 'Q'
            solve(board, row + 1, n)
            board[row][col] = '.'  

n = 4
board = [["." for i in range(n)] for i in range(n)]
solve(board, 0, n)'''


'''#Tower of Hanoi'''
'''1) move n-1 disks from a to b (C is auxi)
   2) move nth disk from a to c (B is auxi)
   3) move n-1 disks from b to a (A is auxi)'''

'''def tower(disk,source,auxi,dest):
    if(disk==1):
        print("Move {} from {} to {}".format(disk,source,dest))
        return
    else:
        tower(disk-1,source,dest,auxi)
        print("Move {} from {} to {}".format(disk,source,dest))
        tower(disk-1,auxi,source,dest)
disk= int(input("Enter the number:"))
print("Steps involved are:")
tower(disk,'A','B','C')'''
