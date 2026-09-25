"""RGB Mixed"""

def main():
    """RGB Mixed"""
    r1,g1,b1 = map(int, input().split())
    r2,g2,b2 = map(int, input().split())
    red = (r1 + r2) // 2
    green = (g1 + g2) // 2
    blue = (b1 + b2) // 2
    print(f"{red} {green} {blue}")
main()
