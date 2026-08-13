"""ปราสาท"""

import math
def main():
    """ให้คุณเขียนโปรแกรมรับหมายเลขห้องที่คุณอยู่ และหาว่าถ้าจะเดินทางไปถึงห้อง 1 \
    จะต้องพังกำแพงน้อยที่สุดกี่กำแพง"""
    room = int(input())
    floor = math.ceil(math.sqrt(room))
    if room == 1:
        print(0)
    elif ((floor ** 2) - room) % 2 == 1:
        print((2 * (floor - 1)) - 1)
    else:
        print(2 * (floor - 1))
main()
