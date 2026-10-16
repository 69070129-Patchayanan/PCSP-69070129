"""Shorten"""

def main():
    """Shorten"""
    num_list = []
    total = []
    while True:
        num = int(input())
        if num == -1:
            break
        num_list.append(num)

    if num_list:
        start = num_list[0]
        for i in range(1, len(num_list)):
            if num_list[i] != num_list[i-1] + 1:
                if start == num_list[i-1]:
                    total.append(str(start))
                else:
                    total.append(f"{start}-{num_list[i-1]}")
                start = num_list[i]

        if start == num_list[-1]:
            total.append(str(start))
        else:
            total.append(f"{start}-{num_list[-1]}")

    print(", ".join(total))
main()
