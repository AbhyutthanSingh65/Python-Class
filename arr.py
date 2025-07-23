a = [[[11, 22, 33],
      [44, 55, 66],
      [77, 12, 32]],

     [[41, 42, 43],
      [52, 54, 56],
      [98, 97, 95]]]

"""for i in range(3):
    print(a[1][1][i])

for i in range(1,3):
    for j in range(0,3):
        print(a[0][i][j], end=" ")"""
        
for i in range(0,2):
    for j in range(0,3):
        for k in range(0,3):
            print(a[i][j][k], end=" ")
        
        print() 
    print("-------------------------------------------")      
