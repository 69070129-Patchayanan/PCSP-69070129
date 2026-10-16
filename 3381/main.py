"""Points Sorting"""

def main():
    """Points Sorting"""
    t = int(input())

    for _ in range(t):
        n = int(input())
        points = []

        for _ in range(n):
            x, y = input().split()
            points.append([int(x), int(y)])

        for i in range(n):
            for j in range(0, n - i - 1):
                s1 = points[j][0] + points[j][1]
                s2 = points[j + 1][0] + points[j + 1][1]

                if (s1 > s2) or (s1 == s2 and points[j][1] < points[j + 1][1]):
                    points[j], points[j + 1] = points[j + 1], points[j]

        for point in points:
            print(f"{point[0]} {point[1]}")

main()
