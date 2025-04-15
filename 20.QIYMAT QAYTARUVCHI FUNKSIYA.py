#QIYMAT QAYTARUVCHI FUNKSIYA

def mijoz_info(ism, familiya, tug_yil, yoshi, tug_joy, email='', tel_raqam=''):
    """Foydalanuvchi haqida ma'lumot beruvchi funksiya"""
    mijoz = {'ism':ism,
              'familiya':familiya,
              'tug_yil':tug_yil,
              'yosh':yoshi,
              'tug_joy':tug_joy,
              'email':email,
              'tel_raqam':tel_raqam}
    return mijoz

print("Mijoz haqida ma'lumotlarni kiriting.")

mijoz_1 = mijoz_info('Bekzod', 'Saidullayev', 1995, 30, 'Tashkent')
print(mijoz_1)



print("Mijozlar haqida ma'lumot beruvchi funksiya.")
mijozlar = []
while True:
    ism = input("Ismingizni kiriting: ")
    familiya = input("Familiyangizni kiriting: ")
    tug_yil = input("Tug'ilgan yilingizni kiriting: ")
    yoshi = input("Yoshingizni kiriting: ")
    tug_joy = input("Tug'ilgan joyingizni kiriting: ")
    email = input("Email manzilingizni kiriting: ")
    tel_raqam = input("Telefon raqamingizni kiritng: ")
    mijozlar.append(mijoz_info(ism, familiya, tug_yil, yoshi, tug_joy))
    javob = input("Davom etasizmi? (ha/yo'q')")
    if javob != 'ha':
        break
    
for mijoz in mijozlar:
    print(f"{ism.title()} {familiya.title()} {tug_yil}-yilda tug'ilgan. Telefon raqami {tel_raqam}")
    

def son_kirit(son1,son2,son3):
    """3 ta son kiritib, ulardan kattasini chiqaruvchi funksiya"""
    max = son1
    if max<=son2:
        max = son2
    if max <= son3:
        max = son3
    return max
son_kirit(5, 3, 16)

def aylana_inf(radius):
    aylana = {'radius' : radius,
              'diametr' : radius*2,
              'aylana_uzun' : 2*3.14*radius,
              'yuzi' : 3.14*(radius**2)
              }
    return aylana

aylana_inf(14)



def tub_sonlar(oraliq1,oraliq2):
    """Oraliqdagi tub sonlarni aniqlovchi funksiya"""
    sonlar = []
    for son in list(range(oraliq1,oraliq2+1)):
        if son%2!=0:
            sonlar.append(son)
    return sonlar

tub_sonlar(5, 16)
        


def fibon_son(son):
    """Foydalanuvchidan son qabul qili, u son qiymaticha Fibonacci ketma ketligini chiqaruvchi funksiya"""
    sonlar = []
    for x in range(son):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar
print(fibon_son(15))