# for TAKRORLASH OPERATORI

ismlar = ["Asqarbek","Akmal","Behruz","Saidakmal","Diyorbek"]
for ism in ismlar:
    print(f"Assalomu Alaykum {ism.title()}. Sogliqlariringiz yaxshimi?")
print("Sizlarni iftorlikka kutaman.")

ismlar = ["Asqarbek","Akmal","Behruz","Saidakmal","Diyorbek"]
for ism in ismlar:
    print(f"Assalomu Alaykum {ism.title()}. Sogliqlariringiz yaxshimi?")
print(f"Kod {len(ismlar)} martta qaytarildi.")

t_sonlar = list(range(11,100,2))
for n in t_sonlar:
    print(f"{n} ning kubi {n**3} ga teng.")

kinolar = []
for n in range(5):
    kinolar.append(input(f"{n+1}-kino nomini kiriting: "))
print(kinolar)    

dostlar=[]
savol = int(input("Bugun nechta odam bilan uchrashdingiz: "))
for n in range(savol):
    dostlar.append(input(f"{n+1}-uchrashgan odmning ismini kiriting:"))
print(dostlar)