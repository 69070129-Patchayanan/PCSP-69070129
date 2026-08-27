"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

def main():
    """divided d remainder r"""
    numA = int(input())
    numB = int(input())
    divided = int(input())
    remainder = int(input())
    total = 0

    for i in range(numA, numB+1):
        d = i % divided
        total += d == remainder
    print(total)
main()
