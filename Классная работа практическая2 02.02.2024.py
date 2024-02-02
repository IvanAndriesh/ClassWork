a = 10
b = 20
if a > b and a > 5:
    print("Истина")
else:
    print("Ложь")
    if b > a and b > 15:
        print("Истина")
        if a == b and a == 10:
            print("Истина")
        else:
            print("Ложь")
            if a < b and a < 30:
                print("Истина")
    else:
        print("Ложь")
if a > b or a > 5:
    print("Истина")
    if b > a or b > 15:
        print("Истина")
        if a == b or a == 15:
            print("Истина")
        else:
            print("Ложь")
            if a > b or a < 5:
                print("Истина")
            else:
                print("Ложь")
    else:
        print("Ложь")
