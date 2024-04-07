# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# solve by myself but not working, this code was correct but terminal not working
wheather = str(input("what is Wheather "))

if wheather == "Sunny":
    print("Go for a walk")
elif wheather == "Rainy":
    print("Read a book")
elif wheather == "Snowy":
    print("Build a snowman")

# solution from hitesh
# weather = str(input("what is weather "))

# if weather == "Sunny":
#     activity = "Go for a walk"
# elif weather == "Rainy":
#     activity = "Read a book"
# elif weather == "Snowy":
#     activity = "Build a snowman"

# print(activity)

# this code written by chatgpt
weather = input("What is the weather? ")

if weather == "Sunny":
    activity = "Go for a walk"
elif weather == "Rainy":
    activity = "Read a book"
elif weather == "Snowy":  # Corrected typo here
    activity = "Build a snowman"
else:
    activity = "Stay indoors"

print(activity)

