# FUNKSIYA

def tug_yil(ism,yosh):
    """Foydalanuvchi ism va yoshini so'rab, uning tug'ilgan yilini aniqlovchi funksiya."""
    print(f"Assalomu Alaykum {ism.title()}, siz {2025-yosh}-yilda tug'ilgansiz.")
tug_yil("Bekzod", 30)


def kvad_kub(son):
    """Foydalanuvchidan son olib, uni kvadrat va kubini aniqlovchi funksiya"""
    print(f"{son} ning kvadrati {son**2}.\n"
          f"{son} ning kubi {son**3}.")
kvad_kub(5)


def toq_juft(son):
    """Sonning toq yoki juftligini aniqlovchi funksiya"""
    if son%2!=0:
        print(f"{son} juft son emas.")
    else:
        print(f"{son} juft son.")
toq_juft(5)


def taqqos(x,y):
    """Foydalanuvchidan ikkita son olib ularni taqqoslovchi funksiya"""
    if x<y:
        print(f"{x}<{y}")
    else:
        print(f"{x}<{y}")
taqqos(8, 16)


def taqqos(x,y):
    """Foydalanuvchidan ikkita son olib ulardan kattasini chiqaruvchi funksiya"""
    if x<y:
        print(f"Sonlarning kattasi {y}")
    else:
        print(f"Sonlarning kattasi {x}")
taqqos(5, 3)


def dar_oshir(x,y):
    """Foydalanuvchidan x va y son olib, x**y ni aniqlash funksiyasi"""
    print(f"{x} ning {y}-darajasi {x**y} bo'ladi.")
dar_oshir(5, 2)


def dar_oshir(x,y=2):
    """Foydalanuvchidan x va y son olib, x**y ni aniqlash funksiyasi"""
    print(f"{x} ning {y}-darajasi {x**y} bo'ladi.")
dar_oshir(5, 3)
dar_oshir(3)


def qol_bol(x):
    for n in range(2,11):
        if x%n!=0:
            print(f"{x} soni {n} soniga bo'linmaydi.")
        else:
            print(f"{x} soni {n} soniga bo'linadi.")
qol_bol(16)