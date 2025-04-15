# SONLAR
son = int(input("Istalgan son kiririting:\n>>>"))
print(son, ' ning kvadrati ', (son**2), ' ga teng.')
print(son, ' ning kubi ', (son**3), ' ga teng.')

yosh = int(input("Yoshingiz nechada? \n>>>"))
t_yil = 2025-yosh
print('Siz ', t_yil, '-yilda tug\'ilgansiz.')


a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"{a} + {b} =", a+b)
print(f"{a} - {b} =", a-b)
print(f"{a} x {b} =", a*b)
print(f"{a} : {b} =", a/b)

aka = int(input("Aka tug'ilgan yilingizni kiriting:\n>>>"))
uka = int(input("Uka tug'ilgan yilingizni kiriting:\n>>>"))
farq = uka - aka
print("Aka ukadan",farq,'yosh katta ekan!')

print("To'g'ri burchakli uchuburchakning gipotenuzasini hisoblovchi dastur.")
a = int(input("1-katetning qiymati:\n>>>"))
b = int(input("2-katetning qiymati\n>>>"))
gip = (a**2+b**2)**(1/2)
print(f"Katetlari {a} va {b} bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi:",gip)