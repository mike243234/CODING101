Zander = float(input("Enter Zander Length in cm: "))
def notify():
    print("Release the fish to the water")
    print("The required length to keep the fish is 42 cm or larger")
if Zander >= 42:
    print("You can keep the fish")
else :
   notify()