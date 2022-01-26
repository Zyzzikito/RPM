if __name__ == "__main__":
    a = int(input("Введите число A (Ax^2+bx+c)"))
    b = int(input("Введите число B (ax^2+Bx+c)"))
    c = int(input("Введите число C (ax^2+bx+C)"))
    D = b**2-4*a*c
    x1 = (-b+D**(1/2))/(2*a)
    x2 = (-b-D**(1/2))/(2*a)
    if D >= 0:
        if D == 0:
            print("X=", x1)
        else:
            print("X1=", x1, "X2=", x2)
    else:
        print("Нет корней")
