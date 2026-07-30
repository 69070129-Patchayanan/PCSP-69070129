"""Bill"""

def main():
    """คำนวนหาจำนวนเงินที่ลูกค้าต้องจ่ายหลังจากรวมค่าบริการและ VAT เรียบร้อยแล้ว"""
    cost = int(input())
    service = cost * 10 / 100
    vat = 7 / 100
    total = (((cost + service) * vat) + (cost + service))

    if service <= 50:
        print(f"{((50 + cost) * vat) + (50 + cost):.2f}")
    elif service >= 1000:
        print(f"{((1000 + cost) * vat) + (1000 + cost):.2f}")
    else:
        print(f"{total:.2f}")
main()
