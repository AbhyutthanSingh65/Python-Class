def area_circle():
    r = int(input("Enter the radius: "))
    print("The area of the circle is", r * r * 3.14)

def area_square():
    side = int(input("Enter the side: "))
    print("The area of the square is", side * side)

def area_triangle():
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    print("The area of the triangle is", 0.5 * base * height)

def area_rectangle():
    length = int(input("Enter one side: "))
    breadth = int(input("Enter the other side: "))
    print("The area of the rectangle is", length * breadth)

def area():
    while True:
        print("\nChoose a shape to calculate area:")
        print("1. Circle")
        print("2. Square")
        print("3. Triangle")
        print("4. Rectangle")
        print("0. Exit")
        
        choice = int(input("Enter your choice (0-4): "))
        
        if choice == 0:
            break
        match choice:
            case 1:
                area_circle()
            case 2:
                area_square()
            case 3:
                area_triangle()
            case 4:
                area_rectangle()
            case _:
                print("Invalid choice! Please try again.")

    print("Thank you")

area()
