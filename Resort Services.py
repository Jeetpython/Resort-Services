#Let"s create a resort service counter
print("Welcome to Jeet's Resort's service center.")
name = input("May I know your name please? ")
print("Yes " + name + ", what do you want? ")
services = "Laundry", "Room cleaning", "Water park ticket."
service = input(services)
if service == "Laundry" or "laundry" :
    price = str(100)

if service == "Room cleaning" or "room cleaning" :
    price = str(300)
    
if service == "Water park ticket" or "water park ticket" :
    price = str(500)

print("Here's your " + service + " bill. Your total is $" + price + ".")
print("If you have any enquiries or doubts.")
print("You can refer it to us. Bye.")

    

