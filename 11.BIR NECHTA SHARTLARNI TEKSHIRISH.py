# BIR NECHTA SHARTLARNI TEKSHIRISH

son = int(input("Juft son kiriting: "))
if son%2 == 0:
    print("Raxmat!")
else:
    print("Toq son kiritidingiz, iltimos juft son kiririting.")

yosh = int(input("Iltimos, yoshingizni kiriting: "))
if yosh <= 4 or yosh >=60:
    price = 0
elif yosh<18:
    price = 10000
elif yosh>18:
    price = 2000
print(f"Sizga kirish {price} so'm")

print("Sonlarni taqqoslaymiz!")
son1 = int(input("Birinchi sonni kiriting: "))
son2 = int(input("Ikkinchi sonni kiriting: "))
if son1 == son2:
    print("Sonlar teng.")
elif son1 < son2:
    print(f"{son1} < {son2}")
else:
    print(f"{son1} > {son2}")

mahsulotlar = ['olma','non','tuxum','sut','banan','tvorog','choy','qaymoq','anjir','asal']
print("Savatga kamida 5 ta mahsulot kiriting.")
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting: "))
for mah in savat:
    if mah.lower() in mahsulotlar:
        print(f"{mah.title()} do'konda bor.")
    else:
        print(f"{mah.title()} do'konimizda yo'q")

mahsulotlar = ['olma','non','tuxum','sut','banan','tvorog','choy','qaymoq','anjir','asal']
print("Savatga kamida 5 ta mahsulot kiriting.")
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting: "))
    
bor_mah = []
yoq_mah = []
for mah in savat:
    if mah in mahsulotlar:
        bor_mah.append(mah)
    else:
        yoq_mah.append(mah)
        
if yoq_mah:
    for mah in yoq_mah:
        print(f"{mah} mahsuloti do'konimizda yo'q.")
else:
    print("Barcha mahsulotlar do'konimizda bor.")
    

foydalanuvchilar = ['ali','admin','noname','loginhave','bekzodbek']
login = input("Yangi login kiriting: ")
if login in foydalanuvchilar:
    print("Kiritgan loginingiz mavjud, boshqa login kiriting.")
else:
    print("Sizning yangi loginingiz tasdiqlandi, tashakkur.")


son = int(input("Biror butun son kiririntg: "))
for n in range(2,11):
    if son%n==0:
        print(f"{son} {n} ga qoldiqsiz bo'linadi.")