"""Message Forward"""

def main():
    """Message Forward"""
    info = input().split()
    n_std = int(info[0])
    start_std = int(info[1])

    forward = [0]
    for _ in range(n_std):
        forward.append(int(input()))

    visited = set()
    curr = start_std
    count = 0

    while curr and curr not in visited:
        visited.add(curr)
        count += 1
        curr = forward[curr]
    print(count)
main()
