""" x = ["this", "sentence"]
print(len("this sentence")) 
x = float(1.23) 
y =float(3)
print(x, y) """
""" numbers = [1, 2, 3, 4]
print(numbers[1]) """
""" friend_comes = True
money = True

def and_movies(friend, money):
    if friend and money:
        print("Going to the movies")
and_movies(friend_comes, money) """

""" friend_comes = True
money = True

def or_movies(friend, money):
    if friend or money:
        print("Going to the movies")
and_movies(friend_comes, money) """

""" day_of_week = input("What day is it?")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect")

print( 4 % 2)
# remainder is output """

""" def factor(x, y):
    if x % y:
        print("y is a factor of x")
factor(6734, 64) """
""" rideHeightOK = input("Are you tall enough?")
if rideHeightOK == "yes":
    print("heightOK")
withAdult = input("Are you with an adult?")
if withAdult == "yes":
    print("withAdult") """

rideHeightOK = True
withAdult = True
healthHold = False
if rideHeightOK == False:
    print("not tall enough")
else:
    print("tallenough")

if withAdult == True:
    print("riding with an adult")
else:
    print("without adult")

if healthHold == True:
    print("health restriction flagged")
else: 
    print("no health restriction flagged")
    
canride = (rideHeightOK or withAdult) and (not healthHold)
print(f"yes{canride}")