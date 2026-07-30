"""Seasons"""

def main():
    """เขียนโปรแกรมแสดงฤดูกาลสําหรับเดือนและวันที่กําหนด"""
    month = input()
    day = input()

    if month == "3" and int(day) >= 21:
        print("spring")
    elif month == "6" and int(day) >= 21:
        print("summer")
    elif month == "9" and int(day) >= 21:
        print("fall")
    elif month == "12" and int(day) >= 21:
        print("winter")
    elif month in ["1", "2", "3"]:
        print("winter")
    elif month in ["4", "5", "6"]:
        print("spring")
    elif month in ["7", "8", "9"]:
        print("summer")
    elif month in ["10", "11", "12"]:
        print("fall")
main()
