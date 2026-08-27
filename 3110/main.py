"""Express Delivery War"""

def main():
    """Express Delivery War"""
    ad1,ad2 = input().split()
    weight = float(input())

    if ad1 == "BKK" and ad2 == "CNX":
        print(f"{10 + (30 * weight):.2f}")
    elif ad1 == "CNX" and ad2 == "UBP":
        print(f"{15 + (40 * weight):.2f}")
    elif ad1 == "UBP" and ad2 == "BKK":
        print(f"{20 + (40 * weight):.2f}")
    elif ad1 == "BKK" and ad2 == "PKT":
        print(f"{25 + (50 * weight):.2f}")
    elif ad1 == "PKT" and ad2 == "CNX":
        print(f"{30 + (60 * weight):.2f}")
    elif ad1 == "UBP" and ad2 == "PKT":
        print(f"{40 + (70 * weight):.2f}")
    else:
        print("Error")
main()
