print(">")

x = 5
print("Lets see what numbers I have in my pocket!")
print("I count just one........I thought I had more numbers??????????")
print(">")

if x == 5:
    print("Our number is 5!")
    print("Yep, that's definitively a 5.")
    print("I am pretttyyyy sure that's a 5...")
    print("Okay now I am doubting, let me see!")
    print(">")

y = x + 2
print("Oh I found another one!")
print("I have two numbers in my pocket!")
print("I have a", x, "and a", y)
print(">")

if y == 7:
    print("I knew there was another number!")
print("Let's see if I can get another number out of my pocket!")
print(">")

z = x + y
print("I have a", x, "a", y, "and a", z)
print("that's three whole numbers!")
print(">")

if z == 12:
    print("So many numbers I have :D")
    print(">")

print("I am going to put them all in a list!")
numbers = [x, y, z]
print("I have a list of numbers!")
print("I have a", numbers)
print("I am going to add another number to my list!")
numbers.append(4)
print("Now I have a", numbers)
print(">")

print("I have about enough numbers for today. Bye!")
print(">")
