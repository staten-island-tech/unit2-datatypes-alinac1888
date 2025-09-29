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
""" canride = ()
rideHeightOK = input("Are you tall enough?")
if rideHeightOK == "Yes":
    "Yes" = True
    print() """

# withAdult = input("Are you riding with an adult?")
# if withAdult == "Yes":
#     print("riding with an adult")
# else:
#     print("without adult")
# healthHold = input("Do you have health restrictions?")
# if healthHold == "Yes":
#     print("health restriction flagged")
# else: 
#     print("no health restriction flagged")
#      or "riding with an adult" = True) and (not "no health restriction flagged")
# print("Yes you can ride")


# number = 100
# if number % 2 == 0:
#         print(f"{number} is even")
# else:
#         print(f"{number} is odd")

# bill = 120

# service = input("How was the service?")
# if service == "Great":
#     print(f"Tip = 25%, Total Cost = {bill * 1.25}")

# elif service == "Good":
#     print(f"Tip = 20%, Total Cost = {bill * 1.2}")

# elif service == "Okay":
#     print(f"Tip = 15%, Total Cost = {bill * 1.15}")

# elif service == "Bad":
#     print(f"Tip = 0%, Total Cost = {bill}")

# x = 100
# y = 6
# if x % y == 0:
#      print(f"{y} is a factor of {x}")
# else:
#      print(f"{y} is not a factor of {x}")
    
# count = 10
# while count >= 1:
#     print("this is a count number", count)
#     count = count - 1

x = 120
y = 180
z = 60
gcf = x % z == 0 and y % z == 0
while gcf != 0:
    