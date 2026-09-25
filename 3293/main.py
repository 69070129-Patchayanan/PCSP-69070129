"""BigFrame"""

def main():
    """BigFrame"""
    text_list = []
    for _ in range(5):
        text_list.append(input().strip())
    frame = max(len(text) for text in text_list)
    print("*" * (frame + 4))
    for text in text_list:
        print(f"* {text + " " * (frame - len(text))} *")
    print("*" * (frame + 4))
main()
