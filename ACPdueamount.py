def subtract(a,b):
    return(a-b)

bill=float(input("Enter your bill costs: ")) 
paid=float(input("Enter the amount of money you have: "))

if bill==paid:
    print("Thank you for shopping!")
elif paid>bill:
    print("The change we owe you is: ", subtract(paid,bill))
elif paid<bill:
    print("You still owe us: ", subtract(bill,paid))






