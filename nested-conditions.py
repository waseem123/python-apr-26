# if CONDITION:
#     if CONDITION:
#         statements
#     else:
#         statements
# else:
#     statements

age = int(input('ENTER YOUR AGE - '))

if age>=18:
    voterid = input('DO YOU HAVE VOTER ID? (Y-YES | N-NO) - ')
    if voterid =='Y':
        print("CONGRATULATIONS! YOU CAN VOTE.")
    else:
        print("SORRY! YOU CAN NOT VOTE.")
else:
    print(f"YOU ARE NOT ELIGIBLE. COME FOR VOTE AFTER {18-age} YEARS.")