"""Point collecting game"""

def main():
    """Point collecting game"""
    amount = int(input())
    total = 0

    for _ in range(amount):
        symbol = input()
        if symbol == "+":
            total += 10
        if symbol == "-":
            total += -5
    print(total)
main()
