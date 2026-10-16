"""Giraffe"""

def main():
    """Giraffe"""
    giraffe = int(input())
    height_list = []
    count = 0
    for _ in range(giraffe):
        height = int(input())
        height_list.append(height)

    if giraffe == 1:
        count = 1
    else:
        for i in range(giraffe):
            if not i and (height_list[i] > height_list[i + 1]):
                count += 1
            elif (i == (giraffe - 1)) and (height_list[i] > height_list[i - 1]):
                count += 1
            elif (height_list[i] > height_list[i - 1]) and (height_list[i] > height_list[i + 1]):
                count += 1
    print(count)
main()
