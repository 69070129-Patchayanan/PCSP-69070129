"""Ink"""

import math
def main():
    """อยากทราบว่าบ้านของพวกเขาจะถูกน้ำท่วมในวินาทีที่เท่าใด"""
    S,N = input().split()
    for _ in range(int(N)):
        Xi,Yi = input().split()
        r = (int(Xi) ** 2) + (int(Yi) ** 2)
        sec = (r * 3.1416) / int(S)
        print(math.ceil(sec))
main()
