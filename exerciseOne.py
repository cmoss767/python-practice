weight = float(input("weight: "))

weightType = input("(K)g or (L)bs: ")

if weightType.upper() == "L":
    print("Weight in Kg: " + str(weight * 0.45))
elif weightType.upper() == "K":
    print("Weight in Lbs: " + str(weight / 0.45))
