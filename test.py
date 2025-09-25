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
if rideHeightOK == False:
    print("not tall enough")
else:
    print("tallenough")

withAdult = input("Are you riding with an adult?")
if withAdult == True:
    print("riding with an adult")
else:
    print("without adult")

healthHold = input("Do you have health restrictions?")
if healthHold == True:
    print("health restriction flagged")
else: 
    print("no health restriction flagged")
    
canride = ("tall enough" or "riding with an adult") and (not "no health restriction flagged")
print(f"yes{canride}") """

number = 100
if number % 2 == 0:
        print(f"{number} is even")
else:
        print(f"{number} is odd")

bill = 120

service = input("How was the service?")
if service == "Great":
    print(f"Tip = 25%, Total Cost = {bill * 1.25}")

elif service == "Good":
    print(f"Tip = 20%, Total Cost = {bill * 1.2}")

elif service == "Okay":
    print(f"Tip = 15%, Total Cost = {bill * 1.15}")

elif service == "Bad":
    print(f"Tip = 0%, Total Cost = {bill}")

input = 100
numb = 6
if input % numb == 0:
     print(f"{numb} is a factor of {input}")
else:
     print(f"{numb} is not a factor of {input}")