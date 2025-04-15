#FUNKSIYA VA RO'YXAT

def katta_harf(matnlar):
    """Foydalanuvchidan matn qabul qilib har bir so'zni katta harflarda chiqaruvchi funksiya"""
    matn = []
    while matnlar:
        soz = matnlar.pop()
        matn.append(soz.title())
    return matn

ismlar = ['asqar','akmal','alisher']
print(katta_harf(ismlar[:]))        
        
    
def katta_harf(matnlar):
    for n in range(len(matnlar)):
        matnlar[n]=matnlar[n].title()

ismlar = ['asqar','akmal','alisher']
katta_harf(ismlar)
print(ismlar)
    

def katta_harf(matnlar):
    matnlar = matnlar[:]
    for n in range(len(matnlar)):
        matnlar[n]=matnlar[n].title()
    return matnlar

ismlar = ['asqar','akmal','alisher']
yangi_ism = katta_harf(ismlar)
print(ismlar)
print(yangi_ism)



def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

talabalar= ['asqar','akmal','alisher']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)
