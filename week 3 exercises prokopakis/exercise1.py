colors = ["Red", "Green", "White", "Blue", "Violet"]

user_choice = input("Enter the color you want: ")

color_available = False


for color in colors:
    if color == user_choice:
        color_available = True

if color_available:
    print("Yes, we have this color.")
else:
    print("Sorry, we dont have this color.")
