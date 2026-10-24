"""B - Fully pair?"""

def main():
    """B - Fully pair?"""
    pair = input()
    result = ""
    seen = ""

    for char in pair:
        if char not in seen:
            seen += char
            if pair.count(char) % 2:
                result += char

    if not result:
        print("fully paired")
    else:
        print(result)
main()
