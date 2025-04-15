#while TSIKLI

savol = ("Yaxshi ko'rgan kitobingizni kiriting.")
savol += ("Dasturni to'xtatish uchun 'exit' deb yozing.\n")
while True:
    kitob = input(savol)
    if kitob == 'exit':
        break
    print("Raxmat!")

savol = ("Yoshingizni kiriting:")
savol += ("Dasturni to'xtatish uchun 'exit' deb yozing.\n")

while True:
    qiymat=input(savol)
    if qiymat =='exit':
        break
    yosh=int(qiymat)
    
    if yosh < 7:
        print("Sziga kirish 7000 so'm")
    elif 7<=yosh<18:
        print("Sizga kiriah 3000 so'm")
    elif 18<=yosh<65:
        print("Sizga kirish 10000 so'm")
    elif yosh>65:
        print("Sizga kirish bepul.")
    
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat)**(0.5)
    print(f"{qiymat} ning ildizi {ildiz} ga teng")