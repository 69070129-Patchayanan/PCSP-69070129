"""Flower"""

def main():
    """Flower"""
    l, n = map(int, input().split())

    band = 0
    total = 0
    diagonal = 1

    while total < n:
        band += 1

        for _ in range(l):
            total += diagonal
            diagonal += 1
    print(band)
main()
