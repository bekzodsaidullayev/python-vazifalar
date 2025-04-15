# STRING (MATN)
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(kocha+" ko'chasi, "+mahalla+" mahallasi, "+tuman+" tumani, "+viloyat+" viloyati")

kocha=input("Ko'changiz nomi?")
mahalla=input("Mahallangiz nomi?")
tuman=input("Tumaningiz nomi?")
viloyat=("Viloyatingiz nomi?")
print(f"{kocha.title()} ko'chasi, {mahalla.title()} mahallasi, {tuman.title()} tumani, {viloyat.title()} viloyati")

kocha=input("Ko'changiz nomi?")
mahalla=input("Mahallangiz nomi?")
tuman=input("Tumaningiz nomi?")
viloyat=("Viloyatingiz nomi?")
print(f"{kocha.title()} ko'chasi, \n{mahalla.title()} mahallasi, \n{tuman.title()} tumani, \n{viloyat.title()} viloyati")   

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
yangi_manzil =(f"{kocha.title()} ko'chasi, {mahalla.upper()} mahallasi, {tuman.lower()} tumani, {viloyat.capitalize()} viloyati")
print(yangi_manzil)
