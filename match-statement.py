print("1. Biryani  - RS. 150")
print("2. Shawarma - RS. 110")
print("3. DK       - RS. 20")
print("4. Tea      - Rs. 15")
print("5. EXIT")
choice = int(input("ENTER YOUR CHOICE - "))

match(choice):
    case 1:
        # logic for biryani
        qty = int(input('ENTER THE QUANTITY OF BIRYANI - '))
        bill = qty * 150
        print(f"YOUR BILL IS RS - {bill}")
    case 2:
        # logic for shawarma
        qty = int(input('ENTER THE QUANTITY OF SHAWARMA - '))
        bill = qty * 110
        print(f"YOUR BILL IS RS - {bill}")
    case 3:
        # logic for DK
        qty = int(input('ENTER THE QUANTITY OF DK - '))
        bill = qty * 20
        print(f"YOUR BILL IS RS - {bill}")
    case 4:
        # logic for Tea
        qty = int(input('ENTER THE QUANTITY OF TEA - '))
        bill = qty * 15
        print(f"YOUR BILL IS RS - {bill}")
    case 5:
        print("THANKS! VISIT AGAIN.")
        exit(0)
    case _:
        print("WRONG INPUT! PLEASE SELECT OPTION BETWEEN 1 TO 4")