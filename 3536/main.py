"""isPrime_large"""

def main(num):
    """isPrime_large"""
    if num <= 1:
        return "NO"
    if num == 2:
        return "YES"
    if not num % 2:
        return "NO"

    limit = int(num ** 0.5)
    for i in range(3, limit + 1, 2):
        if not num % i:
            return "NO"
    return "YES"

n = int(input().strip())
print(main(n))
