# MOSLASHUVCHAN FUNKSIYA (*args, **kwargs)

def kopayt_son(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(kopayt_son(1,5,4,8,))
        

def kopaytir(*sonlar):
    """Foydalanuvchidan ixtiyoriy sonlar qbul qilib, ularni ko'paytmasini chiqaruvchi funksiya"""
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma

print(kopaytir(1,5,8,4))


def talaba_inf(ismi, familiyasi, **malumotlar):
    """Talaba haqida ma'lumot beruvchi funksiya"""
    malumotlar['ism']=ismi
    malumotlar['familiya']=familiyasi
    return malumotlar

talaba1 = talaba_inf("Bekzod", 'Saidullayev', yoshi = 30, tug_yili = 1995, millati = "O'zbek")
print(talaba1)

def mijoz_inf (ismi, yoshi, **malumotlar):
    """Mijoz haqida ma'lumot beruvchi funksiya"""
    malumotlar['ismi']=ismi
    malumotlar['yoshi']=yoshi
    return malumotlar

mijoz1 = mijoz_inf("Bekzod", 30, Turi = 'komfort', xiz_turi = "Soch oldirish")
print(mijoz1)
