def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    else:
        leap = False
    return leap


year = int(input("Enter a year number(in this format XXXX):"))
print(is_leap(year))