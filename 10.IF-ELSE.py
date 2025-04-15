# IF-ELSE

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

ism = input("Admin logoningizni kiriting: ")
if ism.lower() == 'admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print(f"Xush kelibsiz, {ism.title()}!")

print("Ikkita son kiriting:")
son1 = float(input("Birinchi sonnin kiririting: "))
son2 = float(input("Ikkinchi sonnin kiririting: "))
if son1 == son2:
    print("Sonlar ten.")
else:
    print("Sonlar farqlanadi.")

son = float(input("Istalgan son kiriting: "))
if son < 0:
    print("Kiritgan soningiz manfiy!")
else:
    print("Kiritgan soningiz musbat!")

son = float(input("Istalgan son kiriting: "))
if son > 0:
    print(f"{son} ning ildizi {son**(1/2)}")
elif son < 0:
    print("Kiritgan soningiz manfiy!")
else:
    print("Nol qiymatidan ildiz chiqarib bo'lmaydi.")