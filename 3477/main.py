"""Pad Thai"""

def main():
    """Pad Thai"""
    ingredients = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
        "Bean Sprouts", "Noodle", "Chives", "Lime",
        "Egg", "Oil", "Peanuts"
    }
    tastes = {"Sweet", "Sour", "Salty"}

    myingredients = set()
    mytastes = set()

    while True:
        item = input().strip()
        if item == "Cook":
            break
        myingredients.add(item)

    while True:
        taste = input().strip()
        if taste == "End":
            break
        mytastes.add(taste)

    if not myingredients.issubset(ingredients):
        print("This is not Pad Thai!!!")

    elif myingredients != ingredients:
        print("This is bad!")

    else:
        if mytastes == tastes:
            print("Delicious!")
        else:
            print("Not Bad...")

main()
