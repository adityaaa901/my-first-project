age = int(input("Apni age enter kijiye: "))

if age < 18:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")
while True:
    age = int(input("Apni age enter kijiye: "))
    
    if age <= 18:
        print("You are not eligible to vote")
    else:
        print("You are eligible to vote")
    
    # पूछो कि दोबारा check करना है या नहीं
    again = input("Kya dobara check karna hai? (yes/no): ")
    if again.lower() != 'yes':
        print("Thank you!")
        break
    
