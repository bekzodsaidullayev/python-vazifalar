# WHILE, RO'YXATLAR VA LUG'ATLAR

buyurtmalar = []
n=1
while True:
    buyurtma = input(f"{n}-buyurtmangiznin kiriting: ")
    buyurtmalar.append(buyurtma)
    savol = input("Yana buyurtma berasizmi: (ha/yo'q')")
    if savol == 'ha':
        n+=1
        continue
    else:
        break

print("Buyurtmalar ro'yhati:")
for buyurtma in buyurtmalar:
    print(buyurtma.title())
    
print("Mahsulot va ularning ro'yhatini tuzamiz.")
mahsulotlar = {}
ishora = True
while ishora:
    mahsulot = input("Mahsulot nomini kiriting:\n")
    narh = input(f"{mahsulot.title()}ning narhini kiriting:\n")
    mahsulotlar[mahsulot]=int(narh)
    
    savol = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
    if savol == "yo'q":
        ishora = False

for mahsulot, narh in mahsulotlar.items():
    print(f"{mahsulot}ning narhi {narh} so'm.")
        

buyurtmalar = ['shaftoli','olma']
mahsulotlar = {'olma':18500,'olcha':21480,'xurmo':34500}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} do'konimizda mavjud. Narhi {mahsulotlar[buyurtma]}.")
    else:
        print(f"Kechirasiz siznin {buyurtma.title()} mahsulotingiz bizning do'konda yo'q.")