F1 = float(input("Enter the First value: "))
F2 = float(input("Enter the Second value: "))
round_F1 = round(F1,3)
round_F2 = round(F2,3)
if(round_F1 == round_F2):
    print("Equal: ", "  F1 = F2 = ",round_F1)
else:
    print("Not equal:","F1 = ",round_F1,"F2 = ",round_F2)
