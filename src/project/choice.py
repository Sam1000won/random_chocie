import random

def pick_presenter(members):
    presenter = random.choice(members)
    return presenter

def main():
    members = ["백승아","오동균","한지웅","탁정균","이태경","서형원"]
    presenter = pick_presenter(members)
    print(f"발표자: {presenter}")

if __name__ == "__main__":
    main()