"""SurprisingVote"""

def main():
    """มีโอกาสที่จะเกิด Surprising หรือไม่ที่หน้ารีวิวสินค้า"""
    vote = float(input())
    votemax = float(input())
    votemin = vote - (votemax * 2)

    if votemin < 0 and (votemax - 0) > 2:
        print("Surprising")
    elif votemin > 0 and (votemax - votemin) > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
