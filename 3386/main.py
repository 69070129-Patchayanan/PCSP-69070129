"""Duplicate I"""

def main():
    """Duplicate I"""
    group1 = set()
    group2 = set()
    m = int(input())
    n = int(input())
    for _ in range(m):
        id_m = int(input())
        group1.add(id_m)
    for _ in range(n):
        id_n = int(input())
        group2.add(id_n)

    duplicates = group1 & group2

    if not duplicates:
        print("Nope")
    else:
        total = sorted(duplicates, reverse=True)
        for stu_id in total:
            print(stu_id)
main()
