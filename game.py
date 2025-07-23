import random


name1 = input("Enter player 1: ")
name2 = input("Enter player 2: ")

print("Comp has fixed 5 nums in range of 1 to 10")
print("You guys have to guess it .. Ready???")


nums = []
while len(nums) != 5:
    d = random.randint(1, 10)
    if d not in nums:
        nums.append(d)

print("------------------------")


k1 = 0
k2 = 0
player1 = []
player2 = []

# 5 rounds
for i in range(3):
    print("------- ROUND {} -------".format(i + 1))

    # Player 1 guess
    print("Dear {}, guess your choice: ".format(name1))
    ch = int(input())
    player1.append(ch)
    if ch in nums:
        print("-----> CORRECT")
        k1 += 1
    else:
        print("-----> WRONG")

    # Player 2 guess
    print("Dear {}, guess your choice: ".format(name2))
    ch = int(input())
    player2.append(ch)
    if ch in nums:
        print("-----> CORRECT")
        k2 += 1
    else:
        print("-----> WRONG")

# Final Result
print("\n====== GAME OVER ======")
print("{}'s Score: {}".format(name1, k1))
print("{}'s Score: {}".format(name2, k2))

if k1 > k2:
    print("🎉 {} wins!".format(name1))
elif k2 > k1:
    print("🎉 {} wins!".format(name2))
else:
    print("It's a Tie!")
