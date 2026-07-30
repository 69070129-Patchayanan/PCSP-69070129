"""Temperature"""

def main():
    """โปรแกรมรับค่าอุณหภูมิจากหน่วยหนึ่งไปเป็นอีกหน่วยหนึ่งตามที่ได้กำหนดไว้"""
    temp = float(input())
    unit1 = input()
    unit2 = input()
    total1 = 0
    total2 = 0

    if unit1 == "C":
        total1 = temp
    elif unit1 == "K":
        total1 = temp - 273.15
    elif unit1 == "F":
        total1 = ((temp - 32) * 5) / 9
    elif unit1 == "R":
        total1 = ((temp * 5) / 9) - 273.15

    if unit2 == "C":
        total2 = total1
    elif unit2 == "K":
        total2 = total1 + 273.15
    elif unit2 == "F":
        total2 = (total1 * 9) / 5 + 32
    elif unit2 == "R":
        total2 = (total1 + 273.15) * 9 / 5

    print(f"{total2:.2f}")
main()
