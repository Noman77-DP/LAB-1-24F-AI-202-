#Objective: Simulate a simple AI assistant using basic logic.

# 1. Hunger logic
ans = input("Are you feeling hungry? (yes/no): ")
if ans == "yes":
    print("You should eat something.\n")
else:
    print("Keep working.\n")

# 2. Time greeting
hr = int(input("Enter hour (0-23): "))
if hr < 12:
    print("Good Morning")
else:
    print("Good Afternoon\n")

# 3. Simple AI Assistant
name = input("What is your name? ")
print("Hello", name)
like = input("Do you like AI? ")
print("That is good to know!")