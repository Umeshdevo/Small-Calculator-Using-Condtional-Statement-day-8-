num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))

print("\n")

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.division")

print("\n")

choice=int(input("Enter your Choice:"))

print("\n")

if choice==1:
    print("The Answer is:",num1+num2)
elif choice==2:
    print("The Answer is:",num1-num2)
elif choice==3:
    print("The Answer is:",num1*num2)
elif choice==4:
    if num2!= 0:
        print("The Answer is:",num1/num2)
else:
    print("Invalid choice")
