# write aprogram to check if anumber is positive
# num = int(input("Enter a number here : "))
# if num>0:
#     print("It is positive")
# else:
#     print("It is negative")

#write a program to check whether a number is odd or even
# num = int(input("Enter a number here : "))
# if num%2==0:
#     print("It is divisible by two")
# else:
#     print("It is not divisible by two")

# area calculator
# print('''Press 1 to get the area of square
# Press 2 to geat the area of rectangle  
# Press 3 to get the area of circle
# Press 4 to get the area of triangle''')

# choice = int(input("Enter a number between 1-4 : "))

# if choice == 1:
#     side = float(input("Enter the size of side of a square : "))
#     area = side**2
#     print("The area of square is : ", area)
# elif choice == 2:
#     length = float(input("Enter the length : "))
#     breadth = float(input("Enter the breadth : "))
#     area = length * breadth
#     print("The area of rectangle is : ", area)
# elif choice == 3:
#     radius = float(input("Enter the radius : "))
#     area = 3.14 * (radius**2)
#     print("The area of a circle is : ", area)
# elif choice == 4:
#     base = float(input("Enter the base : "))
#     height = float(input("Enter the height : "))
#     area = (base * height)/2
    # print("The area of triangle is : ", area)

# write a program to check whether a letter is vowel or not
letter = input("Enter the letter : ")
if letter in 'aeiou' or 'AEIOU':
    print("The passed letter is vowel")
else:
    print("It is consonant")