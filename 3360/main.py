"""Bread Cutting"""

def bread(total_size, cuts):
    """Bread Cutting"""
    sizes = [cuts[0]]
    for i in range(len(cuts) - 1):
        sizes.append(cuts[i + 1] - cuts[i])
    sizes.append(total_size - cuts[-1])
    return sizes

def main():
    """Bread Cutting"""
    info = input().split()
    w = int(info[0])
    h = int(info[1])

    cut_x = [int(i) for i in input().split()]
    cut_y = [int(i) for i in input().split()]

    w_list = bread(w, cut_x)
    h_list = bread(h, cut_y)

    w_list.sort(reverse=True)
    h_list.sort(reverse=True)

    ans1 = w_list[0] * h_list[0]
    ans2 = max(w_list[0] * h_list[1], w_list[1] * h_list[0])

    print(f"{ans1} {ans2}")

main()
